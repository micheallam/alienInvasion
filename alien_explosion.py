import pygame

class Alien_Explosion(pygame.sprite.Sprite):
    def __init__(self, alien, *groups):
        self.explosionImage1 = pygame.image.load('images/Alien_Explosion1.png')
        self.rect = self.explosionImage1.get_rect()

        self.explosionImage2 = pygame.image.load('images/Alien_Explosion2.png')
        self.rect = self.explosionImage2.get_rect()

        self.explosionImage3 = pygame.image.load('images/Alien_Explosion3.png')
        self.rect = self.explosionImage3.get_rect()

        self.explosionImage4 = pygame.image.load('images/Alien_Explosion4.png')
        self.rect = self.explosionImage3.get_rect()

        self.timer = pygame.time.get_ticks()

    def update(self, current_time, alien):
        passed = current_time - self.timer
        if passed <= 1000:
            self.screen.blit(self.explosionImage1, alien)
        elif passed <= 1200:
            self.screen.blit(self.explosionImage2, alien)
        elif passed <= 1400:
            self.screen.blit(self.explosionImage3, alien)
        elif passed <= 1600:
            self.screen.blit(self.explosionImage4, alien)
        elif passed < 2000:
            self.kill()