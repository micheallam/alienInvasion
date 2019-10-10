import pygame
import random
from pygame.sprite import Sprite

WHITE = (255, 255, 255)
class Alien(Sprite):
    # A class to represent a single alien that is for 10 points

    def __init__(self, ai_game):
        # Initialize the alien and set its starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.font = pygame.font.SysFont(None, 40)
        # Image animation flag
        self.imageFlag = True
        self.flagTimer = 0
        # Mystery/UFO's random score
        self.mysteryScore = [50, 100, 200, 300]
        # Variables for explosion
        self.timer = 0
        self.frame = 1
        self.movingDelay = 20
        self.death_time = 0
        self.death_delay = 25


        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/cactuar.bmp')
        self.rect = self.image.get_rect()

        self.alienIdle = {0: 'images/Alien_Mask1.png',
                          1: 'images/Alien2_Mask1.png',
                          2: 'images/Alien3_Mask1.png',
                          3: 'images/UFO1.png'}

        self.alienMoving = {0: 'images/Alien_Mask2.png',
                            1: 'images/Alien2_Mask2.png',
                            2: 'images/Alien3_Mask2.png',
                            3: 'images/UFO2.png',
                            4: 'images/UFO3.png',
                            5: 'images/UFO4.png'}

        self.alienExplosion = {0: 'images/Alien_Explosion1.png',
                               1: 'images/Alien_Explosion2.png',
                               2: 'images/Alien_Explosion3.png',
                               3: 'images/Alien_Explosion4.png'}

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
        # Swaps between the images
        self.timer += 1
        if self.timer >= self.movingDelay:
            if self.frame == 1:
                self.image = pygame.image.load(self.alienMoving[0])
                self.timer = 0
                self.frame = 2
            elif self.frame == 2:
                self.image = pygame.image.load(self.alienIdle[0])
                self.timer = 0
                self.frame = 1

        # Death timer
        self.death_time += 1
        if self.frame == 5:
            self.image = pygame.image.load(self.alienExplosion[0])
            self.frame = 6
            self.death_time = 0
        elif self.frame == 6 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.alienExplosion[1])
            self.frame = 7
            self.death_time = 0
        elif self.frame == 7 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.alienExplosion[2])
            self.frame = 8
            self.death_time = 0
        elif self.frame == 8 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.alienExplosion[3])
            self.frame = 9
            self.death_time = 0
        elif self.frame == 9 and self.death_time >= self.death_delay:
            self.kill()
            self.timer = 0

    def get_points(self):
        return NotImplementedError()

    def mystery_explosion(self, current_time, alien):
        self.mysteryTimer = pygame.time.get_ticks()
        timepass = current_time - self.mysteryTimer
        self.mysteryScoreText = self.font.render(str(alien.get_points()), True, WHITE)
        if timepass <= 1000:
            self.screen.blit(self.mysteryScoreText, alien)
        elif timepass < 10000:
            self.kill()

class Alien1(Alien):
    # creates alien 1 that gives 10 points
    def __init__(self, ai_game):
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

    def update(self):
        # Move the alien right or left
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x
        # Swaps between the images
        self.timer += 1
        if self.timer >= self.movingDelay:
            if self.frame == 1:
                self.image = pygame.image.load(self.alienMoving[1])
                self.timer = 0
                self.frame = 2
            elif self.frame == 2:
                self.image = pygame.image.load(self.alienIdle[1])
                self.timer = 0
                self.frame = 1

        # Death timer
        self.death_time += 1
        if self.frame == 5:
            self.image = pygame.image.load(self.alienExplosion[0])
            self.frame = 6
            self.death_time = 0
        elif self.frame == 6 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.alienExplosion[1])
            self.frame = 7
            self.death_time = 0
        elif self.frame == 7 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.alienExplosion[2])
            self.frame = 8
            self.death_time = 0
        elif self.frame == 8 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.alienExplosion[3])
            self.frame = 9
            self.death_time = 0
        elif self.frame == 9 and self.death_time >= self.death_delay:
            self.kill()
            self.timer = 0


class Alien3(Alien):
    # creates alien 3 that gives 40 points
    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.image = pygame.image.load('images/Alien3_Mask1.png')


    def get_points(self):
        return 40

    def update(self):
        # Move the alien right or left
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x
        # Swaps between the images
        self.timer += 1
        if self.timer >= self.movingDelay:
            if self.frame == 1:
                self.image = pygame.image.load(self.alienMoving[2])
                self.timer = 0
                self.frame = 2
            elif self.frame == 2:
                self.image = pygame.image.load(self.alienIdle[2])
                self.timer = 0
                self.frame = 1

        # Death timer
        self.death_time += 1
        if self.frame == 5:
            self.image = pygame.image.load(self.alienExplosion[0])
            self.frame = 6
            self.death_time = 0
        elif self.frame == 6 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.alienExplosion[1])
            self.frame = 7
            self.death_time = 0
        elif self.frame == 7 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.alienExplosion[2])
            self.frame = 8
            self.death_time = 0
        elif self.frame == 8 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.alienExplosion[3])
            self.frame = 9
            self.death_time = 0
        elif self.frame == 9 and self.death_time >= self.death_delay:
            self.kill()
            self.timer = 0

class Alien4(Alien):
    # Creates the UFo that gives mystery points
    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.image = pygame.image.load('images/UFO1.png')


    def get_points(self):
        # Returns mystery points using random int
        return random.choice(self.mysteryScore)

    def update(self):
        # Move the alien right or left
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x
        # Swaps between the images
        self.timer += 1
        if self.timer >= self.movingDelay:
            if self.frame == 1:
                self.image = pygame.image.load(self.alienMoving[3])
                self.timer = 0
                self.frame = 2
            elif self.frame == 2:
                self.image = pygame.image.load(self.alienMoving[4])
                self.timer = 0
                self.frame = 3
            elif self.frame == 3:
                self.image = pygame.image.load(self.alienMoving[5])
                self.timer = 0
                self.frame = 4
            elif self.frame == 4:
                self.image = pygame.image.load(self.alienIdle[3])
                self.timer = 0
                self.frame = 1

        # Death timer
        self.death_time += 1
        if self.frame == 5:
            self.image = pygame.image.load(self.alienExplosion[0])
            self.frame = 6
            self.death_time = 0
        elif self.frame == 6 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.alienExplosion[1])
            self.frame = 7
            self.death_time = 0
        elif self.frame == 7 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.alienExplosion[2])
            self.frame = 8
            self.death_time = 0
        elif self.frame == 8 and self.death_time >= self.death_delay:
            self.image = pygame.image.load(self.alienExplosion[3])
            self.frame = 9
            self.death_time = 0
        elif self.frame == 9 and self.death_time >= self.death_delay:
            self.kill()
            self.timer = 0

