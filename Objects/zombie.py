import pygame
import random

from Objects.character import Character

class Zombie(Character):
    def __init__(self, x, y):
        super().__init__(x, y, name='zombie')
        self.speed = 3
        self.direction = random.randint(0, 7)
        self.player_spotted = False

    def random_walk(self, screen, player):
        self.looking_for_player(player)

        if self.player_spotted == False:
            self.direction = random.choice([(self.direction - 1) % 8, self.direction, (self.direction + 1) % 8])

        self.direction_move(screen, self.direction, self.speed)

    def looking_for_player(self, player):
        if self.cell == player.cell:
            self.speed = 6
            self.player_spotted = True
            self.direction = self.chase_direction(player)
        else:
            self.speed = 3
            self.player_spotted = False

    def chase_direction(self, player):
        dx = player.x - self.x
        dy = player.y - self.y

        if dx > 0:
            x_dir = 4
        else:
            x_dir = 0

        if dy > 0:
            y_dir = 6
        else:
            y_dir = 2

        if x_dir == 4 and y_dir == 6: return 5
        if x_dir == 4 and y_dir == 2: return 3
        if x_dir == 0 and y_dir == 6: return 7
        if x_dir == 0 and y_dir == 2: return 1


def spawn_random_zombie(player, cell_maze, zombies):
    valid_cells = []

    for cell in cell_maze:
        dist = abs(cell.row - player.cell.row) + abs(cell.col - player.cell.col)
        if dist >= 3:
            valid_cells.append(cell)

    if not valid_cells:
        return

    chosen = random.choice(valid_cells)
    zx = chosen.xpos + chosen.size // 2
    zy = chosen.ypos + chosen.size // 2

    zombie = Zombie(zx, zy)
    zombie.cell = chosen
    chosen.characters.add(zombie)

    zombies.append(zombie)
