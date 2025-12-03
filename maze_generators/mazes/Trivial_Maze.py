from maze_generators.Maze import *

def generate_maze(m: int, n: int) -> Maze:
    maze = Maze(m, n)
    for i in range(1, m):
        actualize_neighbour(maze.board[(i, 0)], 1)

    for i in range(m):
        for j in range(1, n):
            actualize_neighbour(maze.board[(i, j)], 0)

    return maze