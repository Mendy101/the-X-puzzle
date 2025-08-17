from utils import reconstruct_path

# limit = 995 because Python's default recursion limit is 1000,
# so we set it slightly lower to avoid a RecursionError
def dfs(node, visited=None, limit=995):
    if visited is None:
        visited = set()

    visited.add(tuple(node.board))

    if node.is_goal():
        return reconstruct_path(node)

    if node.depth >= limit:
        return None

    for neighbor in node.get_neighbors():
        if tuple(neighbor.board) not in visited:
            result = dfs(neighbor, visited, limit)
            if result:
                return result

    return None
