from Objects.character import Character, distance_between_characters
import pygame
import math


class Warrior(Character):


    def __init__(self, x, y):
        super().__init__(x, y, name='warrior')
        self.is_attacking = False
        self.attack_cooldown = 1000
        self.last_attack_time = 0
        self.attack_duration = 250
        self.sword_length = 70
        self.sword_width = 5
        self.direction = 0
        self.attack_direction = 0
        self.images = {
            0: pygame.image.load("./Graphics/player/warrior/left.png"),
            1: pygame.image.load("./Graphics/player/warrior/left_up.png"),
            2: pygame.image.load("./Graphics/player/warrior/up.png"),
            3: pygame.image.load("./Graphics/player/warrior/right_up.png"),
            4: pygame.image.load("./Graphics/player/warrior/right.png"),
            5: pygame.image.load("./Graphics/player/warrior/right_down.png"),
            6: pygame.image.load("./Graphics/player/warrior/down.png"),
            7: pygame.image.load("./Graphics/player/warrior/left_down.png"),
            "default": pygame.image.load("./Graphics/player/warrior/default.png")
        }

    def attack(self):
        current = pygame.time.get_ticks()

        if current - self.last_attack_time < self.attack_cooldown:
            return

        mx, my = pygame.mouse.get_pos()
        self.attack_direction = math.atan2(self.y - my, mx - self.x)

        self.last_attack_time = current
        self.is_attacking = True

    def draw(self, screen):
        image = self.images.get(self.direction, self.images.get("default"))

        rect = image.get_rect(center=(self.x, self.y))

        screen.blit(image, rect)

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

        possible_targets = self.cell.get_nearby_characters()

        # cala la logika jest generalnie troche useless, bo istnieja od tego funkcje w pygame, ale to moze poprawie
        # generalnie zmienilem te logika knockbackow w stosunku do tego co bylo
        for character in possible_targets:
            #print("character has been hit", character.name)
            if character != self:
                distance = distance_between_characters(character, self)
                #print("character has been hit", character.name)
                dx = character.x - self.x
                dy = -(character.y - self.y)  # pygame ma Y odwrotnie
                target_angle = math.atan2(dy, dx)

                # różnica między kątem miecza a przeciwnikiem
                angle_diff = abs((target_angle - total_angle + math.pi) % (2 * math.pi) - math.pi)

                if (distance <= self.sword_length and angle_diff < math.radians(10)) or distance <= self.sword_length*1/3:
                    #print("character has been hit", character.name)
                    character.knockback(int(grip_x), int(grip_y), 200)

