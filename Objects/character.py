import pygame
import getId as gi

class Character(object):

    color_selection = {
        'warrior' : (255, 0, 0),
        'archer' : (255, 255, 0),
        'mage' : (0, 0, 255),
        'zombie' : (0, 255, 0),
    }

    def __init__(self, x: int, y: int, name: str):
        self.id = gi.give_id() #to jest spoko do debugowania
        self.x = x
        self.y = y
        self.name = name
        self.color = self.color_selection[name]
        self.cell = None
        self.direction = None
        self.speed = None
        self.hitbox = (self.x, self.y, 10) #na razie modele to kółka więc hitbox jest brany jako x,y i radius kołą

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

    def update(self, screen, x, y):
        self.x = x
        self.y = y

    def move(self, screen, lr, ud): #wektor ruchu left right up down
        #przejśćie w prawo
        if lr>0:
            if self.x+lr >= self.cell.xpos+self.cell.size and self.cell.right_cell and self.cell.right:
                self.update(screen, self.x+lr, self.y)
                self.cell.characters.remove(self)
                self.cell = self.cell.right_cell
                self.cell.characters.append(self)
            else:
                self.update(screen, min(self.x+lr, self.cell.xpos+self.cell.size), self.y)

        #przejście w górę
        if ud<0:
            if self.y+ud <= self.cell.ypos and self.cell.up_cell and self.cell.up:
                self.update(screen, self.x, self.y+ud)
                self.cell.characters.remove(self)
                self.cell = self.cell.up_cell
                self.cell.characters.append(self)
            else:
                self.update(screen, self.x, max(self.y+ud, self.cell.ypos))

        #przejscie w lewo
        if lr<0:
            if self.cell.xpos >= self.x + lr and self.cell.left_cell and self.cell.left:
                self.update(screen, self.x + lr, self.y)
                self.cell.characters.remove(self)
                self.cell = self.cell.left_cell
                self.cell.characters.append(self)
            else:
                self.update(screen, max(self.x + lr, self.cell.xpos), self.y)

        #przejście w dół
        if ud>0:
            if self.y + ud >= self.cell.ypos + self.cell.size and self.cell.down_cell and self.cell.down:
                self.update(screen, self.x, self.y + ud)
                self.cell.characters.remove(self)
                self.cell = self.cell.down_cell
                self.cell.characters.append(self)
            else:
                self.update(screen, self.x, min(self.y + ud, self.cell.ypos+self.cell.size))

    # to bym generalnie wyjebal i dal ogolna funkcje typu get move vector
    def direction_move(self, screen, direction, speed):
        match direction:
            case 0:
                self.move(screen, -speed, 0)
            case 1:
                self.move(screen, -speed, -speed)
            case 2:
                self.move(screen, 0, -speed)
            case 3:
                self.move(screen, speed, -speed)
            case 4:
                self.move(screen, speed, 0)
            case 5:
                self.move(screen, speed, speed)
            case 6:
                self.move(screen, 0, speed)
            case 7:
                self.move(screen, -speed, speed)

    def knockback(self, screen, grip_x, grip_y, distance=100):
        vx = self.x - grip_x
        vy = self.y - grip_y

        length = (vx * vx + vy * vy) ** 0.5
        if length == 0:
            return

        nx = vx / length
        ny = vy / length

        self.move(screen, int(nx * distance), int(ny * distance))