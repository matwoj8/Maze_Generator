def maze_convert(maze):
    new_maze = {}
    for (i, j) in maze.board:
        new_maze[(i, j)] = set()

    for (i, j) in maze.board:
        if maze.board[(i, j)].right:
            new_maze[(i, j)].add((i, j + 1))
            new_maze[(i, j + 1)].add((i, j))
        if maze.board[(i, j)].left:
            new_maze[(i, j)].add((i, j - 1))
            new_maze[(i, j - 1)].add((i, j))
        if maze.board[(i, j)].up:
            new_maze[(i, j)].add((i - 1, j))
            new_maze[(i - 1, j)].add((i, j))
        if maze.board[(i, j)].down:
            new_maze[(i, j)].add((i + 1, j))
            new_maze[(i + 1, j)].add((i, j))
    for pos in new_maze:
        new_maze[pos] = list(new_maze[pos])
    return new_maze