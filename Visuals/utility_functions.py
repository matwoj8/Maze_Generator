import pygame

def draw_cell(screen, cell, zoom, CELL_SIZE, px, py, x, y):
    pass

def write_text(screen, text, x, y, font, color):
    for line in text.split("\n"):
        screen.blit(font.render(line, True, color), (x, y))
        y += font.get_height()

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
    for pos in maze:
        px, py = pos
        walls = [1,1,1,1] # gora, dol, lewo, prawo
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

        nx, ny = current_pos
        pygame.draw.rect(screen, (0, 255, 0),
                         (nx * CELL_SIZE * zoom + x + 2, ny * CELL_SIZE * zoom + y + 2, l - 2, l - 2))

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

def draw_maze_cells(screen, cell_maze: dict, zoom: float, CELL_SIZE: int = 60, x=0, y=0) -> None:
    for cell in cell_maze:
        cx, cy = cell.xpos+x, cell.ypos+y

        l = CELL_SIZE

        pygame.draw.rect(screen, (180, 130, 200),
                         (cx, cy, l, l))

        if not cell.up: pygame.draw.line(screen, (50, 50, 50), (cx, cy), (cx + l, cy), 4)
        if not cell.down: pygame.draw.line(screen, (50, 50, 50), (cx, cy + l), (cx + l, cy + l), 4)
        if not cell.left: pygame.draw.line(screen, (50, 50, 50), (cx, cy), (cx, cy + l), 4)
        if not cell.right: pygame.draw.line(screen, (50, 50, 50), (cx + l, cy), (cx + l, cy + l), 4)

def draw_maze_cells_steps(screen, zoom, CELL_SIZE, current, visited, x=0, y=0) -> None:
    # z jakiegos powodu to sie nie rowno rysuje bez odjecia 8 nie wiem pojecia gdzie ono jest dodane
    pygame.draw.rect(screen, (40, 20, 60),
                     (x+CELL_SIZE-8, y+CELL_SIZE-8, current.n*CELL_SIZE, current.m*CELL_SIZE))

    draw_maze_cells(screen, visited, 1, CELL_SIZE, x, y)

    pygame.draw.rect(screen, (0, 255, 0),
                     (current.xpos + x + 2, current.ypos + y + 2, CELL_SIZE - 2, CELL_SIZE - 2))
