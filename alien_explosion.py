import pygame
from os.path import abspath, dirname

BASE_PATH = abspath(dirname(__file__))
IMAGE_PATH = BASE_PATH + '/images/'
IMG_NAMES = ['Alien_Explosion1',
                         'Alien_Explosion2', 'Alien_Explosion3', 'Alien_Explosion4']
IMAGES = {name: pygame.image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
          for name in IMG_NAMES}

class Alien_Explosion(pygame.sprite.Sprite):
    def __init__(self, alien, *groups):
        super(Alien_Explosion, self).__init__(*groups)
        self.image = pygame.transform.scale(self.get_image(alien.row), (40, 35))
        self.image2 = pygame.transform.scale(self.get_image(alien.row), (50, 45))
        self.rect = self.image.get_rect(topleft=(alien.rect.x, alien.rect.y))
        self.timer = self.timer.get_current_time()

    def get_image(row):
        img_explosion = ['1', '2', '3', '4']
        return IMAGES['images/Alien_Explosion{}'.format(img_explosion[row])]

    def update(self, *args):
        passed = self.timer
        if passed <=100:
            self.settings.screen.blit(self.image, self.rect)
        elif passed <= 200:
            self.settings.screen.blit(self.image2, (self.rect.x - 6, self.rect.y - 6))
        elif 400 < passed:
            self.kill()