import heapq
from utils import reconstruct_path ,manhattan_distance

def a_star(start_node):
    open_list = []
    closed_set = set()
    open_map = {}

    f = manhattan_distance(start_node)
    heapq.heappush(open_list, (f, 0, 0, start_node))
    open_map[tuple(start_node.board)] = f

    while open_list:
        _, g, counter, root = heapq.heappop(open_list)

        if root.is_goal():
            return reconstruct_path(root)
        
        # if the original f is smaller
        if tuple(root.board) not in closed_set:
            closed_set.add(tuple(root.board))
            neighbors = root.get_neighbors()

            for neighbor in neighbors:
                state_tuple = tuple(neighbor.board)
                new_f = manhattan_distance(neighbor) + neighbor.cost
                if (state_tuple not in closed_set) and (state_tuple not in open_map or new_f < open_map[state_tuple]):
                    open_map[state_tuple] = new_f
                    counter += 1
                    heapq.heappush(open_list, (new_f, neighbor.cost, counter, neighbor))

    return None
   