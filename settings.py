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
        self.main_bg = pygame.image.load("images/menu.bmp").convert_alpha()
        self.gameover_bg = pygame.image.load("images/gameover.bmp").convert_alpha()
        # 200, 200, 200
        self.bg_color = pygame.transform.scale(self.bg_color, (self.screen_width, self.screen_height))
        self.main_bg = pygame.transform.scale(self.main_bg, (self.screen_width, self.screen_height))
        self.gameover_bg = pygame.transform.scale(self.gameover_bg, (self.screen_width, self.screen_height))

        # Ship settings
        self.ship_limit = 1

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 100

        # Reads highscore file
        self. HS_FILE = "highscore.txt"

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # The leve score multiplier
        self.levelScoreMultiplier = 1
        # How quickly the alien point values increase
        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Initialize settings that change throughout the game
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.mystery_speed = 3.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1


    def increase_speed(self):
        # Increase speed settings and alien point values
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.levelScoreMultiplier = self.levelScoreMultiplier * self.score_scale
