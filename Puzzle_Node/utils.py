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


def write_output_file(path):
    base_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_path, 'Files', 'output.txt')

    with open(filename, 'w') as f:
        f.write(path)