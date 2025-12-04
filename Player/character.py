import pygame


class Character(object):

    color_selection = {
        'warrior' : (255, 0, 0),
        'archer' : (0, 255, 0),
        'mage' : (0, 0, 255),
    }

    def __init__(self, x: int, y: int, name: str):
        self.x = x
        self.y = y
        self.name = name
        self.color = self.color_selection[name]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

    def update(self, screen, x, y):
        self.x = x
        self.y = y
        self.draw(screen)