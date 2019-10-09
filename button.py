import pygame.font
from settings import Settings

class Button:
 
    def __init__(self, ai_game, msg):
        # Initialize button attributes
        self.settings = Settings()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the button's rect object and place it on the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.settings.screen_height - 150
        
        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # Turn msg into a rendered image and center text on the button
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Highscore_Button(Button):
    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg)
        self.button_color = (255, 0, 0)

        self.rect.centery = 700
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect.centerx = 600
        self.msg_image_rect.centery = 700

class Back_Button(Button):
    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg)
        self.button_color = (205, 0, 0)

        self.rect.centery = 720
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect.centerx = 600
        self.msg_image_rect.centery = 720
