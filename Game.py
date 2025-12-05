import time
import pygame
import sys
import Visuals.utility_functions as utility
import maze_generators.mazes.Hunt_And_Kill_Maze as hak
import maze_generators.mazes.Binary_Tree_Maze as bt
import maze_generators.converter as ct
import maze_generators as mg
import Player.character as character
import text

def start(CELL_SIZE: int) -> None:
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    WIDTH, HEIGHT = screen.get_size()
    pygame.display.set_caption("Maze Generator")

    last_mouse_pos = pygame.mouse.get_pos()
    x, y = 100, 50
    sx, sy = 0, 0
    dragging = False
    zoom = 1

    i = 0
    visited = []
    generated = False
    steps_generated = False

    #ogranicze FPS do 60
    clock = pygame.time.Clock()
    FPS = 60

    background = pygame.image.load("Graphics/background.png")
    extras = pygame.image.load("Graphics/extras.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    extras = pygame.transform.scale(extras, (WIDTH, HEIGHT))

    font = pygame.font.SysFont("comicsans", 30)
    #obecne stany = ["menu", "character_selection", "game"]
    game_state = "menu" # zaczynamy w menu

    chosen_character = ""

    #odczytywanie plikow tekstowych
    with open("text/binary_tree", "r", encoding="utf-8") as f:
        binary_tree_description = f.read()

    with open("text/hunt_and_kill", "r", encoding="utf-8") as f:
        hunt_and_kill_description = f.read()

    def reset_stats():
        nonlocal visited, generated, steps_generated, i
        visited = []
        generated = False
        steps_generated = False
        i = 0
        time.sleep(0.2)

    running = True
    while running:
        clock.tick(FPS)
        # eventy
        for event in pygame.event.get():
            # wylaczanie escapem dla pelnego ekranu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            # wylaczanie zwykle lel
            if event.type == pygame.QUIT:
                running = False

            if game_state == "game":
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


        screen.fill((255, 255, 255))

        if game_state == "menu":
            screen.blit(background, (0, 0))
            if utility.draw_button(screen, "Start Adventure", WIDTH * 0.43, HEIGHT * 0.67, WIDTH * 0.14, HEIGHT * 0.10, font=font):
                game_state = "character_selection"
                time.sleep(0.1)
            if utility.draw_button(screen, "Extras", WIDTH * 0.43, HEIGHT * 0.82, WIDTH * 0.14, HEIGHT * 0.10, font=font):
                game_state = ("extras")
                time.sleep(0.1)
        elif game_state == "character_selection":
            if utility.draw_button(screen, "Back", WIDTH * 0.47, HEIGHT * 0.86, WIDTH * 0.06, HEIGHT * 0.03, font=font):
                game_state = "menu"
                time.sleep(0.1)
            if utility.draw_button(screen, "Warrior", WIDTH * 0.15, HEIGHT * 0.40, WIDTH * 0.15, HEIGHT * 0.30, font=font):
                game_state = "game"
                chosen_character = "warrior"
            if utility.draw_button(screen, "Archer", WIDTH * 0.425, HEIGHT * 0.40, WIDTH * 0.15, HEIGHT * 0.30, font=font):
                game_state = "game"
                chosen_character = "archer"
            if utility.draw_button(screen, "Mage", WIDTH * 0.70, HEIGHT * 0.40, WIDTH * 0.15, HEIGHT * 0.30, font=font):
                game_state = "game"
                chosen_character = "mage"

        elif game_state == "extras":
            screen.blit(extras, (0, 0))
            if utility.draw_button(screen, "Back", WIDTH * 0.47, HEIGHT * 0.86, WIDTH * 0.06, HEIGHT * 0.03, font=font):
                game_state = "menu"
                time.sleep(0.1)
            if utility.draw_button(screen, "Maze Generator Algorithms", WIDTH * 0.4, HEIGHT * 0.20, WIDTH * 0.2, HEIGHT * 0.05, font=font):
                game_state = "extras_maze_generators"
                time.sleep(0.1)

        elif game_state == "extras_maze_generators":

            if utility.draw_button(screen, "Back", WIDTH * 0.47, HEIGHT * 0.86, WIDTH * 0.06, HEIGHT * 0.03, font=font): game_state = "menu"
            if utility.draw_button(screen, "Binary Tree", WIDTH * 0.04, HEIGHT * 0.20, WIDTH * 0.2, HEIGHT * 0.05, font=font): game_state = "extras_maze_generators_binary_tree"
            if utility.draw_button(screen, "Hund And Kill", WIDTH * 0.04, HEIGHT * 0.3, WIDTH * 0.2, HEIGHT * 0.05, font=font): game_state = "extras_maze_generators_hunt_and_kill"
            if utility.draw_button(screen, "Origin Shift", WIDTH * 0.04, HEIGHT * 0.4, WIDTH * 0.2, HEIGHT * 0.05, font=font): game_state = "extras_maze_generators_origin_shift"
            if utility.draw_button(screen, "ALGORYTM KONDZIA", WIDTH * 0.04, HEIGHT * 0.5, WIDTH * 0.2, HEIGHT * 0.05, font=font): game_state = "extras_maze_generators_cos"

        elif game_state == "extras_maze_generators_binary_tree":
            if utility.draw_button(screen, "Back", WIDTH * 0.47, HEIGHT * 0.86, WIDTH * 0.06, HEIGHT * 0.03, font=font):
                game_state = "extras"
                reset_stats()
                continue
            if utility.draw_button(screen, "Binary Tree", WIDTH * 0.04, HEIGHT * 0.20, WIDTH * 0.2, HEIGHT * 0.05, font=font):
                game_state = "extras_maze_generators_binary_tree"
                reset_stats()
                continue
            if utility.draw_button(screen, "Hund And Kill", WIDTH * 0.04, HEIGHT * 0.3, WIDTH * 0.2, HEIGHT * 0.05, font=font):
                game_state = "extras_maze_generators_hunt_and_kill"
                reset_stats()
                continue
            if utility.draw_button(screen, "Origin Shift", WIDTH * 0.04, HEIGHT * 0.4, WIDTH * 0.2, HEIGHT * 0.05, font=font):
                game_state = "extras_maze_generators_origin_shift"
                reset_stats()
                continue
            if utility.draw_button(screen, "ALGORYTM KONDZIA", WIDTH * 0.04, HEIGHT * 0.5, WIDTH * 0.2, HEIGHT * 0.05, font=font):
                game_state = "extras_maze_generators_cos"
                reset_stats()
                continue

            utility.write_text(screen, binary_tree_description, WIDTH * 0.3, HEIGHT * 0.6, font = font, color = (128,128,255))

            if steps_generated is False:
                maze, path = bt.generate_maze(30, 20)
                maze = ct.maze_convert(maze)
                steps_generated = True
                i = 0

            cur = path[i]
            visited.append(cur)
            utility.draw_visited(screen, maze, zoom, 30, cur, visited, WIDTH * 0.4, HEIGHT * 0.1)

            pygame.display.flip()
            time.sleep(0.1)
            i += 1
            if i >= len(path):
                i = 0
                visited = []
                time.sleep(1)


        elif game_state == "extras_maze_generators_hunt_and_kill":
            if utility.draw_button(screen, "Back", WIDTH * 0.47, HEIGHT * 0.86, WIDTH * 0.06, HEIGHT * 0.03, font=font):
                game_state = "extras"
                reset_stats()
                continue
            if utility.draw_button(screen, "Binary Tree", WIDTH * 0.04, HEIGHT * 0.20, WIDTH * 0.2, HEIGHT * 0.05, font=font):
                game_state = "extras_maze_generators_binary_tree"
                reset_stats()
                continue
            if utility.draw_button(screen, "Hund And Kill", WIDTH * 0.04, HEIGHT * 0.3, WIDTH * 0.2, HEIGHT * 0.05, font=font):
                game_state = "extras_maze_generators_hunt_and_kill"
                reset_stats()
                continue
            if utility.draw_button(screen, "Origin Shift", WIDTH * 0.04, HEIGHT * 0.4, WIDTH * 0.2, HEIGHT * 0.05, font=font):
                game_state = "extras_maze_generators_origin_shift"
                reset_stats()
                continue
            if utility.draw_button(screen, "ALGORYTM KONDZIA", WIDTH * 0.04, HEIGHT * 0.5, WIDTH * 0.2, HEIGHT * 0.05, font=font):
                game_state = "extras_maze_generators_cos"
                reset_stats()
                continue

            utility.write_text(screen, hunt_and_kill_description, WIDTH * 0.3, HEIGHT * 0.6, font=font, color=(128, 128, 255))

            if steps_generated is False:
                maze, path = hak.generate_maze(30, 20)
                maze = ct.maze_convert(maze)
                steps_generated = True
                i = 0

            cur = path[i]
            visited.append(cur)
            utility.draw_visited(screen, maze, zoom, 30, cur, visited, WIDTH * 0.4, HEIGHT * 0.1)

            pygame.display.flip()
            time.sleep(0.1)
            i += 1
            if i >= len(path):
                i = 0
                visited = []
                time.sleep(1)


        elif game_state == "extras_maze_generators_origin_shift":
            if utility.draw_button(screen, "Back", WIDTH * 0.47, HEIGHT * 0.86, WIDTH * 0.06, HEIGHT * 0.03, font=font): game_state = "extras"
            if utility.draw_button(screen, "Binary Tree", WIDTH * 0.04, HEIGHT * 0.20, WIDTH * 0.2, HEIGHT * 0.05, font=font): game_state = "extras_maze_generators_binary_tree"
            if utility.draw_button(screen, "Hund And Kill", WIDTH * 0.04, HEIGHT * 0.3, WIDTH * 0.2, HEIGHT * 0.05, font=font): game_state = "extras_maze_generators_hunt_and_kill"
            if utility.draw_button(screen, "Origin Shift", WIDTH * 0.04, HEIGHT * 0.4, WIDTH * 0.2, HEIGHT * 0.05,  font=font): game_state = "extras_maze_generators_origin_shift"
            if utility.draw_button(screen, "ALGORYTM KONDZIA", WIDTH * 0.04, HEIGHT * 0.5, WIDTH * 0.2, HEIGHT * 0.05, font=font): game_state = "extras_maze_generators_cos"


        elif game_state == "game":

            keys = pygame.key.get_pressed()

            speed = 3

            if keys[pygame.K_a]:
                sx -= speed
            if keys[pygame.K_d]:
                sx += speed
            if keys[pygame.K_w]:
                sy -= speed
            if keys[pygame.K_s]:
                sy += speed

            if dragging:
                mx, my = pygame.mouse.get_pos()
                dx = mx - last_mouse_pos[0]
                dy = my - last_mouse_pos[1]
                x += dx
                y += dy
                last_mouse_pos = (mx, my)
            if not generated:
                player = character.Character(sx, sy, chosen_character)
                maze, path = hak.generate_maze(50, 50)
                maze = ct.maze_convert(maze)
                generated = True

            utility.draw_maze(screen, maze, zoom, CELL_SIZE, x, y)
            player.update(screen, sx, sy)

        pygame.display.flip()

    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    start(60)