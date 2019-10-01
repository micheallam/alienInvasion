import pygame
from pygame import Surface
from pygame.sprite import Sprite

class Barrier(Sprite):
    # Creates the barrier between aliens and ship

    def __init__(self, size, color, row, column):
        Sprite.__init__(self)
        self.height = size
        self.width = size
        self.color = color
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.row = row
        self.column = column

