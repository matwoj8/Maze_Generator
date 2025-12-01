def maze_convert(maze):
    new_maze = {}
    for (i, j) in maze:
        new_maze[(i, j)] = set()
        if maze[(i, j)].right != None:
            new_maze[(i, j)].add((i, j + 1))
        if maze[(i, j)].left != None:
            new_maze[(i, j)].add((i, j - 1))
        if maze[(i, j)].up != None:
            new_maze[(i, j)].add((i, j - 1))
        if maze[(i, j)].down != None:
            new_maze[(i, j)].add((i, j + 1))
    return new_maze