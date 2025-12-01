def maze_convert(maze):
    new_maze = {}
    for (i, j) in maze:
        new_maze[(i, j)] = set()
        if maze[(i, j)].right != None:
            new_maze[(i, j)].add((i, j + 1))
        if maze[(i, j)].left != None:
            new_maze[(i, j)].add((i, j - 1))
        if maze[(i, j)].up != None:
            new_maze[(i, j)].add((i-1, j))
        if maze[(i, j)].down != None:
            new_maze[(i, j)].add((i+1, j))
    for pos in new_maze:
        new_maze[pos] = list(new_maze[pos])
    return new_maze