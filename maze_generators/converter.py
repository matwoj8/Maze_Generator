def maze_convert(maze):
    new_maze = {}
    for (i, j) in maze.board:
        new_maze[(i, j)] = set()
        if maze.board[(i, j)].right:
            new_maze[(i, j)].add((i, j + 1))
        if maze.board[(i, j)].left:
            new_maze[(i, j)].add((i, j - 1))
        if maze.board[(i, j)].up:
            new_maze[(i, j)].add((i-1, j))
        if maze.board[(i, j)].down:
            new_maze[(i, j)].add((i+1, j))
    for pos in new_maze:
        new_maze[pos] = list(new_maze[pos])
    return new_maze