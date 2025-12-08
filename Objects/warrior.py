from Objects.character import Character
import pygame
import math


class Warrior(Character):
    def __init__(self, x, y):
        super().__init__(x, y, name='warrior')
        self.is_attacking = False
        self.attack_cooldown = 1000
        self.last_attack_time = 0
        self.attack_duration = 250
        self.sword_length = 30
        self.sword_width = 5
        self.direction = 0
        self.attack_direction = 0

    def attack(self):
        current = pygame.time.get_ticks()

        if current - self.last_attack_time < self.attack_cooldown:
            return

        mx, my = pygame.mouse.get_pos()
        self.attack_direction = math.atan2(self.y - my, mx - self.x)

        self.last_attack_time = current
        self.is_attacking = True

    def draw_sword(self, screen):
        if not self.is_attacking:
            return

        now = pygame.time.get_ticks()
        time = now - self.last_attack_time
        if time >= self.attack_duration:
            self.is_attacking = False
            return

        progress = time / self.attack_duration
        swing_angle = -45 + progress * 90

        base_angle = self.attack_direction
        total_angle = base_angle + math.radians(swing_angle)

        grip_x = self.x + math.cos(base_angle) * 5
        grip_y = self.y - math.sin(base_angle) * 5
        tip_x = grip_x + math.cos(total_angle) * self.sword_length
        tip_y = grip_y - math.sin(total_angle) * self.sword_length

        pygame.draw.line(screen, (180, 180, 180), (int(grip_x), int(grip_y)), (int(tip_x), int(tip_y)), self.sword_width)
        #pygame.draw.circle(screen, (0, 0, 0), (int(grip_x), int(grip_y)), 3) To jest rekojesc to debugowania, moze kiedy tez sie przyda



