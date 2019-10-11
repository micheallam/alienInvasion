import pygame
 
from pygame.sprite import Sprite
 
class Ship(Sprite):
    # A class to manage the ship
 
    def __init__(self, ai_game):
        # Initialize the ship and set its starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        GRAY = (230, 230, 230)
        white = (255, 255, 255)

        self.frame = 0
        self.time = 0
        self.deathFlag = False
        self.death_time = 0
        self.death_delay = 20

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.image.set_colorkey(GRAY)
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Loads the ship's explosion images and get its rect.
        self.shipDeath = {0: 'images/shipexplosion1.png',
                          1: 'images/shipexplosion2.png',
                          2: 'images/shipexplosion3.png',
                          3: 'images/shipexplosion4.png',
                          4: 'images/shipexplosion5.png',
                          5: 'images/shipexplosion6.png',
                          6: 'images/shipexplosion7.png',
                          7: 'images/shipexplosion8.png'}

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update the ship's original image

        if self.frame == 0:
            self.image = pygame.image.load('images/ship.png')


        # Update the ship's position based on movement flags
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        # Draw the ship at its current location
        if self.frame == 5:
            self.image = pygame.image.load(self.shipDeath[0])
            self.frame = 6
            self.death_time = 0
        elif self.frame == 6 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.shipDeath[1])
            self.frame = 7
            self.death_time = 0
        elif self.frame == 7 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.shipDeath[2])
            self.frame = 8
            self.death_time = 0
        elif self.frame == 8 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.shipDeath[3])
            self.frame = 9
            self.death_time = 0
        elif self.frame == 9 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.shipDeath[4])
            self.frame = 10
            self.death_time = 0
        elif self.frame == 10 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.shipDeath[5])
            self.frame = 11
            self.death_time = 0
        elif self.frame == 11 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.shipDeath[6])
            self.frame = 12
            self.death_time = 0
        elif self.frame == 12 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.shipDeath[7])
            self.death_time = 0
            self.deathFlag = False
            self.frame = 0

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # Center the ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
