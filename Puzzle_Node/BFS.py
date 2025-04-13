from collections import deque

from utils import reconstruct_path


def bfs(start_node):
    queue = deque([start_node]) 
    visited = set()              

    while queue:
        current = queue.popleft()

        if current.is_goal():
            return reconstruct_path(current)

        visited.add(current)

        for neighbor in current.get_neighbors():
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

    return "No solution"
