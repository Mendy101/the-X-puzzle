from utils import reconstruct_path

def ids(start_node):
    depth = 0
    while True:
        print(f"Trying depth limit: {depth}")
        result = depth_limited_search(start_node, depth)
        if result is not None:
            return reconstruct_path(result)
        depth += 1

def depth_limited_search(node, depth_limit):
    if node.is_goal():
        return node
    if depth_limit == 0:
        return None

    for neighbor in node.get_neighbors():
        result = depth_limited_search(neighbor, depth_limit - 1)
        if result is not None:
            return result
    return None


