from maze_generators.Cell import Cell

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

def convert_to_cells(maze, x, y):
    new_maze_dict = {}

    for pos, node in maze.board.items():
        i, j = int(pos[0]), int(pos[1])
        new_cell = Cell(node, 60, x, y)
        new_maze_dict[(i, j)] = new_cell

    for (i, j), cell in new_maze_dict.items():
        cell.left_cell = new_maze_dict.get((i, j - 1), None)
        cell.right_cell = new_maze_dict.get((i, j + 1), None)
        cell.up_cell = new_maze_dict.get((i - 1, j), None)
        cell.down_cell = new_maze_dict.get((i + 1, j), None)

    return new_maze_dict