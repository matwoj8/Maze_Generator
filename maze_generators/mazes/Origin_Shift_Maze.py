from maze_generators.Maze import *
from random import choice
import maze_generators.mazes.Trivial_Maze as tr


def generate_maze(m: int, n: int, k: int) -> dict:
    maze = tr.generate_maze(m, n)
    position = (0, 0)

    for i in range(k):
        options = find_all_existing_neighbours(maze.board[position])
        if options == []: break
        new_position, direction = choice(options)
        actualize_neighbour(maze.board[position], direction)
        position = new_position

        options = find_all_neighbours(maze.board[position])
        if options == []: break
        direction = choice(options)
        actualize_not_neighbour(maze.board[position], direction)

    return maze