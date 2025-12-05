import pygame

def draw_cell(screen, cell, zoom, CELL_SIZE, px, py, x, y):
    pass

def draw_button(screen, text, x, y, w, h, font, color=(128,128,255)): #mozna jeszcze dac przekierowanie ale bnardziej ogolnie jest tak zrobic ez
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    rect = pygame.draw.rect(screen, color, (x, y, w, h), border_radius=5)

    if rect.collidepoint(mouse) and click[0] == 1:
        return True

    text = font.render(text, True, (0,0,0))
    screen.blit(text, (x + (w - text.get_width()) // 2,
                      y + (h - text.get_height()) // 2))
    return False



def draw_maze(screen, maze: dict, zoom: float, CELL_SIZE: int = 60, x: int = 200, y: int = 200) -> None:
    x += 100
    y += 50
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

        pygame.draw.rect(screen, (55, 23, 77),
                         (px * CELL_SIZE * zoom + x, py * CELL_SIZE * zoom + y, l, l))

        nx, ny = current_pos
        pygame.draw.rect(screen, (0, 255, 0),
                         (nx * CELL_SIZE * zoom + x+2, ny * CELL_SIZE * zoom + y+2, l-2, l-2))

        if pos in visited:
            pygame.draw.rect(screen, (151, 99, 207),
                             (px * CELL_SIZE * zoom + x, py * CELL_SIZE * zoom + y, l, l))

            for cell in maze[pos]:
                cx, cy = cell

                #pygame.draw.line(screen, (255, 0, 0), (px * int(zoom * CELL_SIZE) + x, py * int(zoom * CELL_SIZE) + y),
                #                 (cx * int(zoom * CELL_SIZE) + x, cy * int(zoom * CELL_SIZE) + y), 4)

                if cx == px+1 and cy == py: walls[3] = 0
                elif cx == px-1 and cy == py: walls[2] = 0
                elif cx == px and cy == py+1: walls[1] = 0
                elif cx == px and cy == py-1: walls[0] = 0

                cx = int(px*CELL_SIZE*zoom + x)
                cy = int(py*CELL_SIZE*zoom + y)

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