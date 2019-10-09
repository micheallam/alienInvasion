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
        self.shipexplosion1 = pygame.image.load('images/shipexplosion1.png')
        self.rect = self.shipexplosion1.get_rect()
        self.shipexplosion2 = pygame.image.load('images/shipexplosion2.png')
        self.rect = self.shipexplosion2.get_rect()
        self.shipexplosion3 = pygame.image.load('images/shipexplosion3.png')
        self.rect = self.shipexplosion3.get_rect()
        self.shipexplosion4 = pygame.image.load('images/shipexplosion4.png')
        self.rect = self.shipexplosion4.get_rect()
        self.shipexplosion5 = pygame.image.load('images/shipexplosion5.png')
        self.rect = self.shipexplosion5.get_rect()
        self.shipexplosion6 = pygame.image.load('images/shipexplosion6.png')
        self.rect = self.shipexplosion6.get_rect()
        self.shipexplosion7 = pygame.image.load('images/shipexplosion7.png')
        self.rect = self.shipexplosion7.get_rect()
        self.shipexplosion8 = pygame.image.load('images/shipexplosion8.png')
        self.rect = self.shipexplosion8.get_rect()

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
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
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # Center the ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def ship_explosion(self, currenttime, ship):
        self.gameTimer = pygame.time.get_ticks()
        passed = currenttime - self.gameTimer
        if passed <= 1000:
            self.screen.blit(self.shipexplosion1, ship)
        elif passed <= 3000:
            self.screen.blit(self.shipexplosion2, ship)
        elif passed <= 5000:
            self.screen.blit(self.shipexplosion3, ship)
        elif passed <= 7000:
            self.screen.blit(self.shipexplosion4, ship)
        elif passed <= 10000:
            self.screen.blit(self.shipexplosion5, ship)
        elif passed <= 15000:
            self.screen.blit(self.shipexplosion6, ship)
        elif passed <= 20000:
            self.screen.blit(self.shipexplosion7, ship)
        elif passed <= 25000:
            self.screen.blit(self.shipexplosion8, ship)
        elif passed < 30000:
            self.kill()
