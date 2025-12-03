import pygame

def draw_cell(screen, cell, zoom, CELL_SIZE, px, py, x, y):
    pass

def draw_maze(screen, maze: dict, zoom: float, CELL_SIZE: int = 60, x: int = 200, y: int = 200) -> None:
    for pos in maze:
        px, py = pos
        walls = [1,1,1,1] # gora, dol, lewo, prawo
        for cell in maze[pos]:
            cx, cy = cell

            pygame.draw.line(screen, (255, 0, 0), (px * int(zoom * CELL_SIZE) + x, py * int(zoom * CELL_SIZE) + y),
                             (cx * int(zoom * CELL_SIZE) + x, cy * int(zoom * CELL_SIZE) + y), 4)

            if cx == px+1 and cy == py: walls[3] = 0
            elif cx == px-1 and cy == py: walls[2] = 0
            elif cx == px and cy == py+1: walls[1] = 0
            elif cx == px and cy == py-1: walls[0] = 0

            cx = int(px*CELL_SIZE*zoom + x - zoom*CELL_SIZE/2)
            cy = int(py*CELL_SIZE*zoom + y - zoom*CELL_SIZE/2)
            l = int(zoom*CELL_SIZE)

        if walls[0]: pygame.draw.line(screen, (50, 50, 50), (cx,cy), (cx+l,cy), 2)
        if walls[1]: pygame.draw.line(screen, (50, 50, 50), (cx,cy+l), (cx+l,cy+l), 2)
        if walls[2]: pygame.draw.line(screen, (50, 50, 50), (cx,cy), (cx,cy+l), 2)
        if walls[3]: pygame.draw.line(screen, (50, 50, 50), (cx+l,cy), (cx+l,cy+l), 2)


def draw_visited(screen, maze, zoom, CELL_SIZE, current_pos, visited, x, y):
    for pos in maze:
        px, py = pos
        walls = [1,1,1,1] # gora, dol, lewo, prawo
        l = int(zoom * CELL_SIZE)

        pygame.draw.rect(screen, (171, 173, 40),
                         (px * CELL_SIZE * zoom + x - l / 2, py * CELL_SIZE * zoom + y - l / 2, l, l))

        nx, ny = current_pos
        pygame.draw.rect(screen, (0, 255, 0),
                         (nx * CELL_SIZE * zoom + x - l / 2+2, ny * CELL_SIZE * zoom + y - l / 2+2, l-2, l-2))

        if pos in visited:
            pygame.draw.rect(screen, (151, 99, 207),
                             (px * CELL_SIZE * zoom + x - l / 2, py * CELL_SIZE * zoom + y - l / 2, l, l))

            for cell in maze[pos]:
                cx, cy = cell

                #pygame.draw.line(screen, (255, 0, 0), (px * int(zoom * CELL_SIZE) + x, py * int(zoom * CELL_SIZE) + y),
                #                 (cx * int(zoom * CELL_SIZE) + x, cy * int(zoom * CELL_SIZE) + y), 4)

                if cx == px+1 and cy == py: walls[3] = 0
                elif cx == px-1 and cy == py: walls[2] = 0
                elif cx == px and cy == py+1: walls[1] = 0
                elif cx == px and cy == py-1: walls[0] = 0

                cx = int(px*CELL_SIZE*zoom + x - zoom*CELL_SIZE/2)
                cy = int(py*CELL_SIZE*zoom + y - zoom*CELL_SIZE/2)

            if walls[0]: pygame.draw.line(screen, (50, 50, 50), (cx,cy), (cx+l,cy), 4)
            if walls[1]: pygame.draw.line(screen, (50, 50, 50), (cx,cy+l), (cx+l,cy+l), 4)
            if walls[2]: pygame.draw.line(screen, (50, 50, 50), (cx,cy), (cx,cy+l), 4)
            if walls[3]: pygame.draw.line(screen, (50, 50, 50), (cx+l,cy), (cx+l,cy+l), 4)

def maze_dfs_traversal(maze: dict, start: tuple[int, int]) -> list[tuple[int, int]]:
    visited = set()
    path = []

    def dfs(node):
        path.append(node)
        visited.add(node)
        for neighbor in maze.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
                path.append(node)

    dfs(start)
    return path