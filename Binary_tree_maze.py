from random import randint

class Node():
    def __init__(self, left = None, right = None, up = None, down = None, position = None):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.position = position

    def printPosition(self):
        return f"({self.position[0]}, {self.position[1]})"

def generate_maze(m: int, n: int) -> dict:
    maze = {(i, j): Node(position = (i, j)) for i in range(m) for j in range(n)}

    for i in range(m - 1):
        for j in range(n - 1):
            if randint(0, 1) == 0:
                maze[(i, j)].right = maze[(i, j + 1)]
                maze[(i, j + 1)].left = maze[(i, j)]
            else:
                maze[(i, j)].down = maze[(i + 1, j)]
                maze[(i + 1, j)].up = maze[(i, j)]

    for j in range(n - 1):
        maze[(m - 1, j)].right = maze[(m - 1, j + 1)]
        maze[(m - 1, j + 1)].left = maze[(m - 1, j)]

    for i in range(m - 1):
        maze[(i, n - 1)].down = maze[(i + 1, n - 1)]
        maze[(i + 1, n - 1)].up = maze[(i, n - 1)]

    return maze


# def print_maze(maze):
#     for node in maze.values():
#         print(node.printPosition(), node.left, node.right, node.up, node.down)

if __name__ == '__main__':
    maze = generate_maze(3, 4)
    # print_maze(maze)