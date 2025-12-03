import pygame
import sys
import Visuals.utility_functions as utility
import maze_generators.Hunt_and_kill as hak
import maze_generators.Binary_tree_maze as bt
import maze_generators.converter as ct

def start(CELL_SIZE: int) -> None:
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    WIDTH, HEIGHT = screen.get_size()
    pygame.display.set_caption("Maze Generator")

    maze, path = hak.generate_maze(50, 50)
    maze = hak.maze_convert(maze)

    last_mouse_pos = pygame.mouse.get_pos()
    x, y = 200, 200
    dragging = False
    zoom = 1

    running = True
    while running:

        # eventy
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

        screen.fill((255, 255, 255))

        # rysujemy maze
        utility.draw_maze(screen, maze, zoom, CELL_SIZE, x, y)

        # rysowanie maze krok po kroku

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    start(60)