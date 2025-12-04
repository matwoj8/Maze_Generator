import time
import pygame
import sys
import Visuals.utility_functions as utility
import maze_generators.mazes.Hunt_And_Kill_Maze as hak
import maze_generators.mazes.Binary_Tree_Maze as bt
import maze_generators.converter as ct
import maze_generators as mg
import Player.character as character

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

    #ogranicze FPS do 60
    clock = pygame.time.Clock()
    FPS = 60

    background = pygame.image.load("Graphics/background.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    font = pygame.font.SysFont("comicsans", 30)
    #obecne stany = ["menu", "character_selection", "game"]
    game_state = "menu" # zaczynamy w menu

    chosen_character = ""

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
            if utility.draw_button(screen, "Start Adventure", WIDTH/2-150, HEIGHT/2+200, 300, 150, font=font):
                game_state = "character_selection"
                time.sleep(0.1)
        elif game_state == "character_selection":
            if utility.draw_button(screen, "Warrior", WIDTH-1820, HEIGHT-800, 500, 600, font=font):
                game_state = "game"
                chosen_character = "warrior"
            if utility.draw_button(screen, "Archer", WIDTH-1210, HEIGHT-800, 500, 600, font=font):
                game_state = "game"
                chosen_character = "archer"
            if utility.draw_button(screen, "Mage", WIDTH-590, HEIGHT-800, 500, 600, font=font):
                game_state = "game"
                chosen_character = "mage"
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