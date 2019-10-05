import pygame
from pygame.sprite import Sprite
 
class Alien(Sprite):
    # A class to represent a single alien that is for 10 points

    def __init__(self, ai_game):
        # Initialize the alien and set its starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/cactuar.bmp')
        self.rect = self.image.get_rect()

        '''self.explosionImage1 = pygame.image.load('images/Alien_Explosion1.png')
        self.rect = self.explosionImage1.get_rect()

        self.explosionImage2 = pygame.image.load('images/Alien_Explosion2.png')
        self.rect = self.explosionImage2.get_rect()

        self.explosionImage3 = pygame.image.load('images/Alien_Explosion3.png')
        self.rect = self.explosionImage3.get_rect()

        self.explosionImage4 = pygame.image.load('images/Alien_Explosion4.png')
        self.rect = self.explosionImage3.get_rect()'''

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        # Return True if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # Move the alien right or left
        self.x += (self.settings.alien_speed *
                        self.settings.fleet_direction)
        self.rect.x = self.x

    def get_points(self):
        return NotImplementedError()

    '''def alien_explosion(self, current_time, alien):
        self.gameTimer = pygame.time.get_ticks()
        passed = current_time - self.gameTimer
        if passed <= 1000:
            self.screen.blit(self.explosionImage1, alien)
        elif passed <= 1200:
            self.screen.blit(self.explosionImage2, alien)
        elif passed <= 1400:
            self.screen.blit(self.explosionImage3, alien)
        elif passed <= 1600:
            self.screen.blit(self.explosionImage4, alien)
        elif passed < 2000:
            self.kill() '''


class Alien1(Alien):
    # creates alien 1 that gives 10 points
    def __init__(self,ai_game):
        super().__init__(ai_game)
        self.image = pygame.image.load('images/Alien_Mask1.png')

    def get_points(self):
        return 10


class Alien2(Alien):
    # creates alien 2 that gives 20 points
    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.image = pygame.image.load('images/Alien2_Mask1.png')

    def get_points(self):
        return 20


class Alien3(Alien):
    # creates alien 3 that gives 40 points
    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.image = pygame.image.load('images/Alien3_Mask1.png')

    def get_points(self):
        return 40

