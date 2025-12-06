import time
import pygame
import sys
import Visuals.utility_functions as utility
import maze_generators.mazes.Hunt_And_Kill_Maze as hak
import maze_generators.mazes.Binary_Tree_Maze as bt
import maze_generators.converter as ct
import maze_generators as mg

def start(maze, path, n, m):
    CELL_SIZE = 60

    pygame.init()

    # FULLSCREEN
    screen = pygame.display.set_mode((n*CELL_SIZE+100, m*CELL_SIZE+100))
    WIDTH, HEIGHT = screen.get_size()
    pygame.display.set_caption("Maze Generator")

    # Zegar bierzemy, żeby kontrolować framerate, ale na razie nie używam
    # clock = pygame.time.Clock()
    print(WIDTH, HEIGHT)

    #rzeczy do kamery
    last_mouse_pos = pygame.mouse.get_pos()
    x, y = 50, 50
    dragging = False
    zoom = 1

    def draw_maze(maze, zoom, CELL_SIZE):
        for pos in maze:
            px, py = pos
            walls = [1,1,1,1] # gora, dol, lewo, prawo
            l = int(zoom * CELL_SIZE)

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
                l = int(zoom*CELL_SIZE)

            if walls[0]: pygame.draw.line(screen, (50, 50, 50), (cx,cy), (cx+l,cy), 5)
            if walls[1]: pygame.draw.line(screen, (50, 50, 50), (cx,cy+l), (cx+l,cy+l), 5)
            if walls[2]: pygame.draw.line(screen, (50, 50, 50), (cx,cy), (cx,cy+l), 5)
            if walls[3]: pygame.draw.line(screen, (50, 50, 50), (cx+l,cy), (cx+l,cy+l), 5)


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
        draw_maze(maze, zoom, CELL_SIZE)

        #rysowanie maze krok po kroku

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    n, m = 12, 12
    maze, path = hak.generate_maze(n, m)
    maze = mg.converter.maze_convert(maze)
    start(maze, path, n, m)

