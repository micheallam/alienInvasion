import pygame

class Settings:
    # A class to store all settings for Alien Invasion

    def __init__(self):
        #Initialize the game's static settings
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        # Background image
        self.bg_color = pygame.image.load("images/background.bmp").convert_alpha()
        # 200, 200, 200
        self.bg_color = pygame.transform.scale(self.bg_color, (self.screen_width, self.screen_height))

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Initialize settings that change throughout the game
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring for each alien
        self.alien_points = 10
        self.alien2_points = 20
        self.alien3_points = 40

    def increase_speed(self):
        # Increase speed settings and alien point values
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        self.alien2_points = int(self.alien2_points * self.score_scale)
        self.alien3_points = int(self.alien3_points * self.score_scale)
