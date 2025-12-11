from Objects.character import Character, distance_between_characters
import pygame
import math


class Mage(Character):
    def __init__(self, x, y):
        super().__init__(x, y, name="mage")
        self.attack_cooldown = 500
        self.last_attack_time = 0
        self.range = 700
        self.arrow_length = 20
        self.sword_width = 3
        self.direction = 0
        self.attack_direction = 0
        self.images = {
            0: pygame.image.load("./Graphics/player/mage/left.png"),
            1: pygame.image.load("./Graphics/player/mage/left_up.png"),
            2: pygame.image.load("./Graphics/player/mage/up.png"),
            3: pygame.image.load("./Graphics/player/mage/right_up.png"),
            4: pygame.image.load("./Graphics/player/mage/right.png"),
            5: pygame.image.load("./Graphics/player/mage/right_down.png"),
            6: pygame.image.load("./Graphics/player/mage/down.png"),
            7: pygame.image.load("./Graphics/player/mage/left_down.png"),
            "default": pygame.image.load("./Graphics/player/mage/default.png")
        }

    def draw(self, screen):
        image = self.images.get(self.direction, self.images.get("default"))

        rect = image.get_rect(center=(self.x, self.y))

        screen.blit(image, rect)

    def attack(self):
        current = pygame.time.get_ticks()

        if current - self.last_attack_time < self.attack_cooldown:
            return

        mx, my = pygame.mouse.get_pos()
        self.attack_direction = math.atan2(self.y - my, mx - self.x)

        self.last_attack_time = current

        # shot_arrow()