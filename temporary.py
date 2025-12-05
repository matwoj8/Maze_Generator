#okresowe czasowo funkcje których potrzebuje do losowych rzeczy potem je podzioele gdzie mają być
import pygame

from maze_generators.Cell import Cell

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

    return list(new_maze_dict.values())

def draw_maze(screen, cell_maze: dict, zoom: float, CELL_SIZE: int = 60, x: int = 200, y: int = 200) -> None:
    for cell in cell_maze:
        cx, cy = cell.xpos, cell.ypos

        l = int(zoom * CELL_SIZE)

        if not cell.up: pygame.draw.line(screen, (150, 50, 50), (cx, cy), (cx + l, cy), 2)
        if not cell.down: pygame.draw.line(screen, (150, 50, 50), (cx, cy + l), (cx + l, cy + l), 2)
        if not cell.left: pygame.draw.line(screen, (150, 50, 50), (cx, cy), (cx, cy + l), 2)
        if not cell.right: pygame.draw.line(screen, (150, 50, 50), (cx + l, cy), (cx + l, cy + l), 2)



