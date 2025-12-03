from random import randint
from maze_generators.converter import *
from maze_generators.Maze import *

def generate_maze(m: int, n: int) -> dict:
    maze = Maze(m, n)

    for i in range(m - 1):
        for j in range(n - 1):
            if randint(0, 1) == 0:
                maze.board[(i, j)].right = True
                maze.board[(i, j + 1)].left = True
            else:
                maze.board[(i, j)].down = True
                maze.board[(i + 1, j)].up = True

    for j in range(n - 1):
        maze.board[(m - 1, j)].right = True
        maze.board[(m - 1, j + 1)].left = True

    for i in range(m - 1):
        maze.board[(i, n - 1)].down = True
        maze.board[(i + 1, n - 1)].up = True

    return maze


if __name__ == '__main__':
    maze = generate_maze(3, 3)
    new_maze = maze_convert(maze)
    print(new_maze)