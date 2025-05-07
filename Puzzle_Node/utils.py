import os

def reconstruct_path(node):
    path = []
    while node.parent:
        path.append(node.move)
        node = node.parent
    return ''.join(reversed(path))


def read_input_file():
    base_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_path, 'Files', 'input.txt')

    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        algorithm = int(lines[0])
        size = int(lines[1])
        start_state = list(map(int, lines[2].split('-')))
    return algorithm, size, start_state


def manhattan_distance(node):
    distance = 0
    for i in range(len(node.board)):
        if node.board[i] != 0:  
            goal_pos = node.board[i] - 1
            current_row, current_col = divmod(i, node.size)
            goal_row, goal_col = divmod(goal_pos, node.size)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return distance


def write_output_file(path):
    base_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_path, 'Files', 'output.txt')

    with open(filename, 'w') as f:
        f.write(path)