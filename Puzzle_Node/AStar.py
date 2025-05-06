import heapq
from utils import reconstruct_path

goal_pos = {}

def goal_state(n):
    goal = list(range(1, n * n))
    goal.append(0)
    return [goal[i:i + n] for i in range(0, len(goal), n)]


def goal_positions(state):
    global goal_pos
    goal = goal_state(state.size)

    for i in range(len(goal)):
        for j in range(len(goal[0])):
            goal_pos[goal[i][j]] = (i, j)

    return goal_pos


def manhattan_distance(state):
    global goal_pos
    dist = 0
    x = 0
    for i in range(state.size):
        for j in range(state.size):
            val = state.board[x]
            x += 1
            if val != 0:
                gi, gj = goal_pos[val]
                dist += abs(i - gi) + abs(j - gj)
    return dist


def a_star(start_node):
    global goal_pos
    goal_pos = goal_positions(start_node)

    open_list = []
    closed_set = set()

    f = manhattan_distance(start_node)
    g = 0
    heapq.heappush(open_list, (f + g, g, start_node))
    closed_set.add(tuple(start_node.board))

    while open_list:
        h, g, root = heapq.heappop(open_list)

        if root.is_goal():
           print(f"after {root.board}")
           return reconstruct_path(root)
        
        neighbors = root.get_neighbors()
        for neighbor in neighbors:
            state_tuple = tuple(neighbor.board)
            if state_tuple not in closed_set:
                closed_set.add(state_tuple)
                new_f = manhattan_distance(neighbor)
                new_g = g + 1
                heapq.heappush(open_list, (new_g + new_f, new_g, neighbor))

    return None
   