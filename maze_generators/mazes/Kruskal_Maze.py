from random import choice, shuffle
from random import randint
from maze_generators.Maze import *
from maze_generators.converter import *

def generate_maze(m: int, n: int) -> (dict, list):
    maze = Maze(m, n)
    all_sets = []
    for node in maze.board:
        all_sets.append(set({node}))
    shuffle(all_sets)

    path = []

    while len(all_sets) > 1:
        chosen_set = choice(all_sets)
        all_sets.remove(chosen_set)

        other = connect_set(chosen_set, all_sets, maze, path)

        if other:
            new_set = chosen_set.union(other)
            all_sets.remove(other)
            all_sets.append(new_set)

    return maze, path

def connect_set(chosen_set, all_sets, maze, path):
    for node in chosen_set:
        for o_set in all_sets:
            for o_node in o_set:
                neighbours = find_all_nonvisited_neighbours(maze.board, maze.board[node])

                for neighbour_pos, option in neighbours:
                    if o_node == neighbour_pos:
                        path.append(node)
                        path.append(o_node)
                        actualize_neighbours(maze.board[node],maze.board[o_node],option)
                        return o_set
    return None

if __name__ == '__main__':
    maze, path = generate_maze(3, 3)
    new_maze = maze_convert(maze)
    print(new_maze)
    print(path)

