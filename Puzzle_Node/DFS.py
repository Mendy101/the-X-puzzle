import heapq
import sys
from utils import reconstruct_path ,manhattan_distance

def dfs(start_node):

    closed_list = set()
    open_list = set()

    def recurs(node):

        state = tuple(node.board)

        if state in closed_list:
            return None 
        if state in open_list:
            return None 
        
        open_list.add(state)
        
        if node.is_goal():
            return node # returns the final node for route reconstruction
        
        for neighbor in node.get_neighbors():
            neighbor_state = tuple(neighbor.board)
            if neighbor_state in closed_list or neighbor_state in open_list:
                continue

            result = recurs(neighbor)
            if result:
                return result
  
        open_list.remove(state) 
        closed_list.add(state)  
        return None   # No route found from the current intersection

    goal_node = recurs(start_node)
    
    if goal_node:
        return reconstruct_path(goal_node)
    else:
       return "No solution" # if there is no solution at all
    
