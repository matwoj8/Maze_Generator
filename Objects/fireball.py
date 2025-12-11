import pygame


class Fireball(pygame.sprite.Sprite):
    def __init__(self, screen, sx, sy, max_range):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.max_range = max_range
        self.starting_position = (sx, sy)
        self.x = sx
        self.y = sy