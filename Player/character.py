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
        self.cell = None

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

    def update(self, screen, x, y):
        self.x = x
        self.y = y
        self.draw(screen)

    def move(self, screen, lr, ud): #wektor ruchu left right up down
        #przejśćie w prawo
        if lr>0 and self.x <= self.cell.xpos+self.cell.size:
            x_arg = min(self.x+lr, self.cell.xpos+self.cell.size)
            self.update(screen, x_arg, self.y)
            if self.x >= self.cell.xpos+self.cell.size and self.cell.right_cell and self.cell.right:
                self.cell = self.cell.right_cell

        #przejście w górę
        if ud<0 and self.y >= self.cell.ypos:
            y_arg = max(self.y+ud, self.cell.ypos)
            self.update(screen, self.x, y_arg)
            if self.y <= self.cell.ypos and self.cell.up_cell and self.cell.up:
                self.cell = self.cell.up_cell

        #przejscie w lewo
        if lr<0 and self.cell.xpos <= self.x:
            x_arg = max(self.x + lr, self.cell.xpos)
            self.update(screen, x_arg, self.y)
            if self.cell.xpos >= self.x and self.cell.left_cell and self.cell.left:
                self.cell = self.cell.left_cell

        #przejście w dół
        if ud>0 and self.y <= self.cell.ypos+self.cell.size:
            y_arg = min(self.y + ud, self.cell.ypos+self.cell.size)
            self.update(screen, self.x, y_arg)
            if self.y >= self.cell.ypos + self.cell.size and self.cell.down_cell and self.cell.down:
                self.cell = self.cell.down_cell