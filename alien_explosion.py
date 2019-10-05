import pygame
from pygame import *

class Alien_Explosion(pygame.sprite.Sprite):
    def __init__(self, ai_game, *groups):
        super(Alien_Explosion, self).__init__(*groups)
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.explosionImage1 = pygame.image.load('images/Alien_Explosion1.png')
        self.rect = self.explosionImage1.get_rect()

        self.explosionImage2 = pygame.image.load('images/Alien_Explosion2.png')
        self.rect = self.explosionImage2.get_rect()

        self.explosionImage3 = pygame.image.load('images/Alien_Explosion3.png')
        self.rect = self.explosionImage3.get_rect()

        self.explosionImage4 = pygame.image.load('images/Alien_Explosion4.png')
        self.rect = self.explosionImage3.get_rect()

        self.timer = pygame.time.get_ticks()

    def update(self, current_time, *args):
        passed = current_time - self.timer
        if passed <= 100:
            self.screen.blit(self.explosionImage1, self.rect)
        elif passed <= 200:
            self.screen.blit(self.explosionImage2, self.rect)
        elif passed <= 300:
            self.screen.blit(self.explosionImage3, self.rect)
        elif passed <= 400:
            self.screen.blit(self.explosionImage4, self.rect)
        elif passed < 500:
            self.kill()