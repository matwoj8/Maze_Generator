import pygame
import sys
import maze_generators.mazes.Binary_Tree_Maze as bt
import maze_generators.mazes.Trivial_Maze as tr
import maze_generators.mazes.Hunt_And_Kill_Maze as hak
import maze_generators.mazes.Origin_Shift_Maze as os
import maze_generators.converter as ct
import time

pygame.init()

# FULLSCREEN
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Maze Generator")

# Zegar bierzemy, żeby kontrolować framerate, ale na razie nie używam
# clock = pygame.time.Clock()
print(WIDTH, HEIGHT)

# przykladowa
maze, path = hak.generate_maze(10, 10)
maze = hak.maze_convert(maze)
#print(maze)
#print(path)

CELL_SIZE = 60

#rzeczy do kamery
last_mouse_pos = pygame.mouse.get_pos()
x, y = 200, 200
dragging = False
zoom = 1

def draw_maze(maze, zoom, CELL_SIZE, current_pos, visited):
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

def dfs_maze(maze, start):
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

#path = dfs_maze(maze, (0,0))
#print(path)
i = 0
visited = []

# Main Game Loop
running = True
while running:

    #eventy
    for event in pygame.event.get():
        # wylaczanie escapem dla pelnego ekranu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # wylaczanie zwykle lel
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            last_mouse_pos = pygame.mouse.get_pos()
            dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False

        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                zoom *= 1.1
                zoom = min(4, zoom)
            else:
                zoom /= 1.1
                zoom = max(0.1, zoom)

    if dragging:
        mx, my = pygame.mouse.get_pos()
        dx = mx - last_mouse_pos[0]
        dy = my - last_mouse_pos[1]
        x += dx
        y += dy
        last_mouse_pos = (mx, my)

    screen.fill((150,150,150))

    #rysujemy maze
    cur = path[i]
    visited.append(cur)
    draw_maze(maze, zoom, CELL_SIZE, cur, visited)

    #rysowanie maze krok po kroku

    pygame.display.flip()
    time.sleep(0.1)
    i += 1
    if i >= len(path):
        i = 0
        visited = []
        time.sleep(1)


pygame.quit()
sys.exit()
