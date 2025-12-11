from Objects.character import Character, distance_between_characters
import pygame
import math

class Archer(Character):
    def __init__(self, x, y):
        super().__init__(x, y, name="archer")
        self.attack_cooldown = 500
        self.last_attack_time = 0
        self.range = 700
        self.arrow_length = 20
        self.sword_width = 3
        self.direction = 0
        self.attack_direction = 0
        self.images = {
            0: pygame.image.load("./Graphics/player/archer/left.png"),
            1: pygame.image.load("./Graphics/player/archer/left_up.png"),
            2: pygame.image.load("./Graphics/player/archer/up.png"),
            3: pygame.image.load("./Graphics/player/archer/right_up.png"),
            4: pygame.image.load("./Graphics/player/archer/right.png"),
            5: pygame.image.load("./Graphics/player/archer/right_down.png"),
            6: pygame.image.load("./Graphics/player/archer/down.png"),
            7: pygame.image.load("./Graphics/player/archer/left_down.png"),
            "default": pygame.image.load("./Graphics/player/archer/default.png")
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

        #shot_arrow()