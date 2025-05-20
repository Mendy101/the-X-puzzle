from utils import reconstruct_path

def ids(start_node):
    depth = 0
    while True:
        print(f"Trying depth limit: {depth}")
        result = depth_limited_search(start_node, depth)
        if result is not None:
            return reconstruct_path(result)
        depth += 1

def depth_limited_search(start_node, depth_limit):
    open_list = [(start_node, 0)]
    open_set = {tuple(start_node.board)}  
    close_set = set()                    

    while open_list:
        current, current_depth = open_list.pop()
        state_key = tuple(current.board)

        open_set.discard(state_key)     
        close_set.add(state_key)         

        if current.is_goal():
            return current

        if current_depth < depth_limit:
            for neighbor in reversed(current.get_neighbors()):
                neighbor_key = tuple(neighbor.board)

                if neighbor_key not in open_set and neighbor_key not in close_set:
                    open_list.append((neighbor, current_depth + 1))
                    open_set.add(neighbor_key)

    return None
