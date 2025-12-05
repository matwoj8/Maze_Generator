import time
import pygame
import sys
import Visuals.utility_functions as utility
import maze_generators.mazes.Hunt_And_Kill_Maze as hak
import maze_generators.mazes.Binary_Tree_Maze as bt
import maze_generators.converter as ct
import maze_generators as mg

def start(maze, path, n, m):
    pygame.init()

    CELL_SIZE = 60

    # FULLSCREEN
    screen = pygame.display.set_mode((n*CELL_SIZE+100, m*CELL_SIZE+100))
    WIDTH, HEIGHT = screen.get_size()
    pygame.display.set_caption("Maze Generator")

    # Zegar bierzemy, żeby kontrolować framerate, ale na razie nie używam
    # clock = pygame.time.Clock()

    #rzeczy do kamery
    last_mouse_pos = pygame.mouse.get_pos()
    x, y = 50, 50
    dragging = False
    zoom = 1

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
        utility.draw_visited(screen,maze, zoom, CELL_SIZE, cur, visited, x, y)

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

if __name__ == "__main__":
    n, m = 12, 10
    maze, path = hak.generate_maze(n, m)
    maze = mg.converter.maze_convert(maze)
    start(maze, path, n, m)
