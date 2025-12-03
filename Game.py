import time
import pygame
import sys
import Visuals.utility_functions as utility
import maze_generators.mazes.Hunt_And_Kill_Maze as hak
import maze_generators.mazes.Binary_Tree_Maze as bt
import maze_generators.converter as ct
import maze_generators as mg

def start(CELL_SIZE: int) -> None:
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    WIDTH, HEIGHT = screen.get_size()
    pygame.display.set_caption("Maze Generator")

    last_mouse_pos = pygame.mouse.get_pos()
    x, y = 0, 0
    dragging = False
    zoom = 1

    i = 0
    visited = []
    generated = False

    font = pygame.font.SysFont("comicsans", 30)
    #obecne stany = ["menu", "generate", "draw_maze", "step_by_step_visualization"]
    game_state = "menu" # zaczynamy w menu

    input_box = pygame.Rect(200, 100, 200, 50)
    input_text = ""
    active = False

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

            if game_state == "draw_maze" or game_state == "step_by_step_visualization":
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

            if game_state == "generate":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    active = input_box.collidepoint(event.pos)

                if event.type == pygame.KEYDOWN and active:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        screen.fill((255, 255, 255))

        if game_state == "menu":
            if utility.draw_button(screen, "Maze generator", WIDTH/2-600, HEIGHT/2, 300, 150, font=font):
                game_state = "generate"
        elif game_state == "generate":

            pygame.draw.rect(screen, (0, 255, 255), input_box, border_radius=5)
            text_surface = font.render(input_text, True, (0, 0, 0))
            screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))


            if utility.draw_button(screen, "Generate Maze", WIDTH/2, HEIGHT/2, 300, 150, font=font):
                game_state = "draw_maze"
            if utility.draw_button(screen, "Step by Step Visualization", WIDTH/2, HEIGHT/2-200, 300, 150, font=font):
                game_state = "step_by_step_visualization"
        else:
            if dragging:
                mx, my = pygame.mouse.get_pos()
                dx = mx - last_mouse_pos[0]
                dy = my - last_mouse_pos[1]
                x += dx
                y += dy
                last_mouse_pos = (mx, my)

            if not generated:
                n, m = input_text.split(' ')
                print(n ,m)
                maze, path = hak.generate_maze(12, 12)
                maze = mg.converter.maze_convert(maze)
                generated = True

            if game_state == "draw_maze":
                utility.draw_maze(screen, maze, zoom, CELL_SIZE, x, y)
            elif game_state == "step_by_step_visualization":
                visited.append(path[i])
                utility.draw_visited(screen, maze, zoom, CELL_SIZE, path[i], visited, x+100, y+50)

                pygame.display.flip()

                i += 1
                time.sleep(0.05)

                if i >= len(path):
                    i = 0
                    visited = []
                    time.sleep(1)

            #utility.draw_maze(screen, maze, zoom, CELL_SIZE, x, y)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    start(60)