import sys
import random
from time import sleep
from os import path


import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from button import Highscore_Button
from button import Back_Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from alien import Alien1
from alien import Alien2
from alien import Alien3
from alien import Alien4
from timer import Timer

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)

class AlienInvasion:

    def __init__(self):
        # Initialize the game, and create game resources
        pygame.init()
        self.settings = Settings()
        self.font = pygame.font.SysFont(None, 100)
        self.ptfont = pygame.font.SysFont(None, 70)

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.backgroundtheme = pygame.mixer.Sound("sounds/Bots 2.wav")
        self.rushedTheme = pygame.mixer.Sound("sounds/BotsRushed.wav")
        self.UFOspawn = pygame.mixer.Sound("sounds/UFO.wav")

        # Set value to True
        self.mainScreen = True
        self.highscoreFlag = False
        self.mysterySpawnFlag = True

        # Random integer for determining mystery spawn
        self.mysterySpawn = 0

        # Alien counter
        self.alienCounter = 0

        # Create an instance to store game statistics,
        #   and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Make the Play button.
        self.play_button = Button(self, "Play")
        self.highscore_button = Highscore_Button(self, "High Score")
        self.back_button = Back_Button(self, "Back")

    def run_game(self):
        # Plays background music
        self.backgroundtheme.play(-1)
        # Start the main loop for the game

        while True:
            if self.mainScreen:
                self._create_main_menu()
                self._check_events()

            elif self.highscoreFlag:
                # plays sound test to see ifit's working
                self._create_highscore()
                self._check_events()

            elif self.stats.game_active:
                current_time = pygame.time.get_ticks()
                self.screen.blit(self.settings.bg_color, (0, 0))
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._check_events()
                self._update_active_screen()

            self._update_screen()

    def _check_events(self):
        # Respond to keypresses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        # Start a new game when the player clicks Play
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        highscore_clicked = self.highscore_button.rect.collidepoint(mouse_pos)
        back_clicked = self.back_button.rect.collidepoint(mouse_pos)
        if highscore_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            self.mainScreen = False
            self.highscoreFlag = True

        if back_clicked and self.highscoreFlag:
            self.highscoreFlag = not self.highscoreFlag
            self.mainScreen = not self.mainScreen

        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()

            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.mainScreen = False
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        # Respond to keypresses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:  # escape exits out of the game
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # Respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        # Create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            # The sound effect for fireing the bullets
            fireBullet = pygame.mixer.Sound("sounds/shoot.wav")
            fireBullet.play()
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        # Update position of bullets and get rid of old bullets
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                 self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Respond to bullet-alien collisions
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, False)

        #pygame.sprite.groupcollide(self.bullets, self.)

        if collisions:
            for aliens in collisions.values():
                for alien in aliens:
                    self.stats.score += alien.get_points() * self.settings.levelScoreMultiplier * len(aliens)
                    self.alienCounter += 1
                    if alien.frame < 5:
                        alien.frame = 5

                    # Play the explosion sound when the get hit
                    alienDeathSound = pygame.mixer.Sound("sounds/invaderkilled.wav")
                    alienDeathSound.play()
                    # end new stuff
                    self.sb.prep_score()
                    self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed() # Also increases the score multiplier
            # Restart the music
            self.rushedTheme.stop()
            self.backgroundtheme.play(-1)

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()
            self.alienCounter = 0

    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
          then update the positions of all aliens in the fleet.
        """
        # Increments mysterySpawn by random integers
        self.randomIncrement = random.randint(0, 70)
        self.mysterySpawn += self.randomIncrement
        alien = Alien4(self)
        # Creates UFO and reset spawner when requirements are met
        if self.mysterySpawn >= 10000 and self.mysterySpawnFlag:
            self._create_mystery_alien(alien)
            self.UFOspawn.play(3)
            # reset spawn number back to 0
            self.mysterySpawn = 0
            self.mysterySpawnFlag = not self.mysterySpawnFlag

        # Aliens will move faster if 15 are killed
        if self.alienCounter == 15:
            self.backgroundtheme.stop()
            self.rushedTheme.play()
            self.settings.alien_speed += 0.1
            self.alienCounter = 0

        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        # Check if any aliens have reached the bottom of the screen
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _ship_hit(self):
        # Respond to the ship being hit by an alien
        self.ship.deathFlag = True
        self.ship.frame = 5
        shipHit = pygame.mixer.Sound("sounds/explosion.wav")
        shipHit.play()
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            
            # Pause.
            sleep(0.5)
        else:
            sleep(0.9)
            # Set active game to false and turn on game over flag
            self.stats.game_active = False
            self.mainScreen = True
            self.backgroundtheme.play(-1)

            pygame.mouse.set_visible(True)

        # Triggers the death animation when ship is hit
        while self.ship.deathFlag:
            self.ship.death_time += 1
            self.ship.blitme()
            pygame.display.flip()

    def _create_fleet(self):
        # Create the fleet of aliens
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                                (3 * alien_height) - ship_height)
        # // keeps the int an int(dumps the digits after the number to keep it an int)
        number_rows = available_space_y // (2 * alien_height)
        
        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                # Change the alien depending on which row it is
                if (row_number == 0):
                    alien = Alien3(self)
                if(row_number == 1):
                    alien = Alien2(self)
                if (row_number == 2 or row_number == 3):
                    alien = Alien1(self)
                self._create_alien(alien_number, row_number, alien)

    # Creates aliens
    def _create_alien(self, alien_number, row_number, alien):
        # Create an alien and place it in the row
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_mystery_alien(self, alien):
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        # Respond appropriately if any aliens have reached an edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        # Drop the entire fleet and change the fleet's direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _create_main_menu(self):
        # Main menu background
        self.screen.blit(self.settings.main_bg, (0, 0))

        # Title screen
        self.title_text_top = self.font.render("SPACE", True, WHITE)
        self.screen.blit(self.title_text_top, (self.settings.screen_width/2 - 100, 50))
        self.title_text_bottom = self.font.render("INVADERS", True, GREEN)
        self.screen.blit(self.title_text_bottom, (self.settings.screen_width / 2 - 150, 110))

        # Creates the image of aliens
        self.Alien1image = pygame.image.load('images/Alien_Mask1.png')
        self.Alien1Scaledimage = pygame.transform.scale(self.Alien1image, (70, 70))
        self.screen.blit(self.Alien1Scaledimage, (460, 250))
        self.Alien2image = pygame.image.load('images/Alien2_Mask1.png')
        self.Alien2ScaledImage = pygame.transform.scale(self.Alien2image, (70, 70))
        self.screen.blit(self.Alien2ScaledImage, (460, 330))
        self.Alien3image = pygame.image.load('images/Alien3_Mask1.png')
        self.Alien3ScaledImage = pygame.transform.scale(self.Alien3image, (70, 70))
        self.screen.blit(self.Alien3ScaledImage, (460, 410))
        self.Alien4image = pygame.image.load('images/UFO1.png')
        self.Alien4ScaledImage = pygame.transform.scale(self.Alien4image, (70, 70))
        self.screen.blit(self.Alien4ScaledImage, (460, 490))

        # How much each alien is worth
        self.Alien1Text = self.ptfont.render("  =   10 PTS", True, WHITE)
        self.screen.blit(self.Alien1Text, (540, 250))
        self.Alien2Text = self.ptfont.render("  =   20 PTS", True, WHITE)
        self.screen.blit(self.Alien2Text, (540, 340))
        self.Alien3Text = self.ptfont.render("  =   40 PTS", True, WHITE)
        self.screen.blit(self.Alien3Text, (540, 420))
        self.Alien4Text = self.ptfont.render("  =  ??? PTS", True, WHITE)
        self.screen.blit(self.Alien4Text, (540, 500))

    def _create_highscore(self):
        font = pygame.font.SysFont("Arial", 72)
        self.screen.blit(self.settings.main_bg, (0, 0))
        # Creates the title of Highscore page
        self.highscore_title_text = self.font.render("HIGHSCORE", True, WHITE)
        self.screen.blit(self.highscore_title_text, (self.settings.screen_width / 2 - 200, 50))

        highscore = open("highscore.txt", "r+")
        for msg in highscore:
            contents = highscore.read()
            scoreOutput = font.render(msg, True, WHITE)
            self.screen.blit(scoreOutput, (self.settings.screen_width / 2 - 100, 100))

        highscore.close()



    def _update_screen(self):
        # Draw the play button if the game is inactive.
        if not self.mainScreen and not self.stats.game_active:
            self.back_button.draw_button()
        elif not self.stats.game_active and not self.highscoreFlag:
            self.play_button.draw_button()
            self.highscore_button.draw_button()

        pygame.display.flip()

    def _update_active_screen(self):
        # Update images on the screen, and flip to the new screen
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
