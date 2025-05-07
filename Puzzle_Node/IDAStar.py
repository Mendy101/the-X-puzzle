from utils import reconstruct_path
def manhattan_distance(node):
    distance = 0
    for i in range(len(node.board)):
        if node.board[i] != 0:  
            goal_pos = node.board[i] - 1
            current_row, current_col = divmod(i, node.size)
            goal_row, goal_col = divmod(goal_pos, node.size)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance



def ida_star(start_node):

    bound = manhattan_distance(start_node)
    
    while True:
       
        result = search(start_node, 0, bound, set())
        
        if isinstance(result, str): 
            return result
        
        if result == float('inf'):  
            return None
        
        bound = result

def search(node, g, bound, visited):
    f = g + manhattan_distance(node)
    if f > bound:
        return f
    if node.is_goal():
        return reconstruct_path(node)

    min_bound = float('inf')
    state_hash = tuple(node.board)
    visited.add(state_hash)

    for neighbor in node.get_neighbors():
        neighbor_hash = tuple(neighbor.board)

        if neighbor_hash in visited:
            continue

        result = search(neighbor, g + 1, bound, visited)
        if isinstance(result, str):
            return result
        min_bound = min(min_bound, result)

    visited.remove(state_hash)  
    return min_bound
