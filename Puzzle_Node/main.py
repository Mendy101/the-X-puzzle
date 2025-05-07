from AStar import a_star
from BFS import bfs
from DFS import dfs
from IDAStar import ida_star
from IDS import ids
from utils import read_input_file, write_output_file


class PuzzleNode:
    def __init__(self, board, size, parent=None, move=None, depth=0, cost=0):
        self.board = board                  
        self.size = size                    
        self.parent = parent               
        self.move = move                   
        self.depth = depth                 
        self.cost = cost                   
        self.zero_index = self.board.index(0)  


    def __str__(self):
        return str(self.board)


    def __lt__(self, other):
        return self.board < other.board 


    def is_goal(self):
        goal = list(range(1, self.size * self.size)) + [0]
        return self.board == goal


    def get_neighbors(self):
        neighbors = []
        row, col = divmod(self.zero_index, self.size)  

        directions = {
            'U': (1, 0),  
            'D': (-1, 0),   
            'L': (0, 1),  
            'R': (0, -1)    
        }

        for move in ['U', 'D', 'L', 'R']:
            dr, dc = directions[move]
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                new_index = new_row * self.size + new_col
                new_board = self.board.copy()

                new_board[self.zero_index], new_board[new_index] = new_board[new_index], new_board[self.zero_index]

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
        for i in range(0, len(self.board), self.size):
            row = self.board[i:i + self.size]
            print(' '.join(str(num).rjust(2) for num in row))
        print()


def main():
    algorithm, size, start_state = read_input_file()
    start_node = PuzzleNode(start_state, size)

    print("algorithm:", algorithm)
    print("board size:", size)
    start_node.display()
    
    path = None
    match algorithm:
        case 1:
            print("running IDS")
            path = ids(start_node)
        case 2:
            print("running BFS")
            path = bfs(start_node)
        case 3:
            print("running A*")
            path = a_star(start_node)
        case 4:
            print("running IDA*")
            path = ida_star(start_node)
        case 5:
            print("running DFS")
            path = dfs(start_node)
        case _:
            print("the algorithm is not supported.")

    if path:
        print("solution found:", path)
        write_output_file(path)   
    else:
        print("no solution found.")
        

if __name__ == "__main__":
    main()