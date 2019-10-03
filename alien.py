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
        self.image = pygame.image.load('images/Alien3_Mask3.png')

    def get_points(self):
        return 40

