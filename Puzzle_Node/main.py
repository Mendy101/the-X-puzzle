from collections import deque  

# מחלקה שמייצגת מצב אחד של לוח המשחק
class PuzzleNode:
    def __init__(self, board, size, parent=None, move=None, depth=0, cost=0):
        self.board = board                  # מצב הלוח 
        self.size = size                    # גודל הלוח 
        self.parent = parent                # מצביע לצומת האב 
        self.move = move                    # התנועה שהובילה למצב הזה (U/D/L/R)
        self.depth = depth                  # עומק הצומת בעץ (כמה תזוזות מההתחלה)
        self.cost = cost                    # עלות כוללת – משמש באלגוריתמים אחרים
        self.zero_index = self.board.index(0)  # מיקום של המשבצת הריקה (0)

    def __eq__(self, other):
        # השוואת שני מצבים (visited set) 
        return self.board == other.board

    def __hash__(self):
        # מאפשר לשים את הצומת ב־set לפי המצב של הלוח
        return hash(tuple(self.board))

    def __str__(self):
        # איך להציג את הצומת אם מדפיסים אותו
        return str(self.board)

    def is_goal(self):
        # בודק אם הגענו למצב המטרה
        goal = list(range(1, self.size * self.size)) + [0]
        return self.board == goal

    def get_neighbors(self):
        # מחזיר רשימת מצבים חוקיים שניתן להגיע אליהם ע"י תזוזת המשבצת הריקה
        neighbors = []
        row, col = divmod(self.zero_index, self.size)  # מחלק את המיקום לשורה ועמודה

        directions = {
            'U': (-1, 0),  # למעלה
            'D': (1, 0),   # למטה
            'L': (0, -1),  # שמאלה
            'R': (0, 1)    # ימינה
        }

        for move, (dr, dc) in directions.items():
            new_row, new_col = row + dr, col + dc

            # בדיקה אם התזוזה בתוך גבולות הלוח
            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                new_index = new_row * self.size + new_col
                new_board = self.board.copy()

                # מחליפים בין הריק למשבצת שנבחרה
                new_board[self.zero_index], new_board[new_index] = new_board[new_index], new_board[self.zero_index]

                # יוצרים צומת שכן חדש
                neighbor_node = PuzzleNode(
                    new_board,
                    self.size,
                    parent=self,
                    move=move,
                    depth=self.depth + 1,
                    cost=self.cost + 1
                )
                neighbors.append(neighbor_node)

        return neighbors

    def display(self):
        # מציג את הלוח בצורה של טבלה 
        for i in range(0, len(self.board), self.size):
            row = self.board[i:i + self.size]
            print(' '.join(str(num).rjust(2) for num in row))
        print()


def read_input_file(filename='input.txt'):
    # קורא את קובץ הקלט ומחזיר את האלגוריתם, גודל הלוח, והמצב ההתחלתי
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        algorithm = int(lines[0])
        size = int(lines[1])
        start_state = list(map(int, lines[2].split('-')))
    return algorithm, size, start_state


def write_output_file(path, filename='output.txt'):
    # כותב את הפלט (רצף הצעדים) לקובץ output.txt
    with open(filename, 'w') as f:
        f.write(path)

# BFS Search Algorithm
def bfs(start_node): 
    queue = deque([start_node])  # תור של מצבים לבדיקה
    visited = set()              # סט של מצבים שכבר ביקרנו בהם

    while queue:
        current = queue.popleft()

        if current.is_goal():
            # אם הגענו למצב המטרה – מחזירים את המסלול
            return reconstruct_path(current)

        visited.add(current)

        # בודקים את כל המצבים האפשריים מהמצב הנוכחי
        for neighbor in current.get_neighbors():
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

    return "No solution"

# DFS Search Algorithm
def dfs (start_node):
    states_stack = [start_node]
    closed_list = set()

    while states_stack:
        current = states_stack.pop()
        if current.is_goal():
            return reconstruct_path(current)
        closed_list.add(current)

        # Add reverse neighbors to preserve order U>D>L>R
        neighbors = current.get_neighbors()
        move_order = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
        neighbors.sort(key=lambda node: move_order[node.move])
        
        for neighbor in reversed(neighbors):
            if neighbor not in closed_list and neighbor not in states_stack:
                states_stack.append(neighbor)
    
    return "No solution" # if there is no solution at all


def reconstruct_path(node):
    # משחזר את המסלול מהצומת האחרון עד ההתחלה
    path = []
    while node.parent:
        path.append(node.move)
        node = node.parent
    return ''.join(reversed(path))  # הופכים את הסדר (כי בנינו אחורה)


def main():
    # קריאת הקלט
    algorithm, size, start_state = read_input_file()
    start_node = PuzzleNode(start_state, size)

    print("input")
    print("algorithm:", algorithm)
    print("board size:", size)
    print("start state:")
    start_node.display()

    # בדיקת האלגוריתם וביצוע בהתאם
    if algorithm == 2:  # BFS
        print("run BFS...")
        path = bfs(start_node)
        print("sloution founded:", path)
        write_output_file(path)

    elif algorithm == 5:  # DFS
        print ("run DFS...")
        path = dfs(start_node)
         print("sloution founded:", path)
        write_output_file(path)
        
    else:
        print("the algorithm is not suppurted.")

# התחלת התוכנית
if __name__ == "__main__":
    main()
