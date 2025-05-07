import heapq
from utils import reconstruct_path ,manhattan_distance

def a_star(start_node):
    open_list = []
    closed_set = set()

    f = manhattan_distance(start_node)
    heapq.heappush(open_list, (f + 0, 0, start_node))
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
   