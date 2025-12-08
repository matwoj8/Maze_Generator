import pygame
import random

from Objects.character import Character

class Zombie(Character):
    def __init__(self, x, y):
        super().__init__(x, y, name='zombie')
        self.speed = 3
        self.direction = random.randint(0, 7)

    def random_walk(self, z, cell_maze, screen):
        z.direction_move(screen, self.direction, self.speed)
        self.direction = random.choice([(self.direction - 1) % 8, self.direction,  (self.direction + 1) % 8])


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
    chosen.characters.append(zombie)

    zombies.append(zombie)
