import rocket_attachment
import utilities
from player import Player
from shield import *


# Note to self, fix player score system, collisions if needed
# Fix enemy kill system, and update system


class Game:
    def __init__(self, width=750, height=650, frames=78, shield_mode=1):
        utilities.GAME_FRAME_RATE = frames
        utilities.GAME_WINDOW = pygame.display.set_mode((width, height), pygame.DOUBLEBUF, 32)

        self.shield_level = shield_mode

        """ Time counter """
        self.time_played = 0

        """ Amount of time game lasts """
        self.game_time = 60 * 3  # In seconds

        """ Creates an all sprites group """
        self.all_sprites = pygame.sprite.Group()

        """ Player group """
        self.player_group = pygame.sprite.Group()

        """ Bullet group """
        self.bullet_group = pygame.sprite.Group()

        """ Shield group """
        self.shield_group = pygame.sprite.Group()

        """ Aliens group """
        self.alien_group = pygame.sprite.Group()

        """ rocket objects group """  # Change to group which contains the AI or Aliens
        self.rockets_group = pygame.sprite.Group()

        """ Creates the player and gives it: a position on the screen, a 
        speed and adds to player group """

        self.player = Player(width, height, utilities.GAME_DELTA)
        self.player.set_position(width / 2, height - 24)
        self.player_group.add(self.player)

    def run(self):
        display_width, display_height = pygame.display.get_window_size()

        """ Updates/Refreshes the game fps_rate per second(s) """
        self.time_played += utilities.GAME_DELTA / 1000.0
        remaining_time = utilities.GAME_DELTA - self.time_played

        if len(self.player_group) == 0:
            utilities.GAME_STATE = 3
            return

        """ Runs the particle graphics() method while the game runs """
        utilities.draw_particles(display_width, display_height, utilities.GAME_COLORS["white"], self.all_sprites)

        """ Runs the alien graphics() method and limits the aliens on the screen """
        while len(self.alien_group) < 60:
            utilities.draw_aliens(display_width, display_height, self.alien_group, self.player, self.player_group)

        keys = pygame.key.get_pressed()

        """ Handles player shoot event """
        self.player.reg_shot(keys, self.alien_group, display_height, self.bullet_group)

        """ Handles events for rocket creation """
        if keys[pygame.K_DOWN]:
            if len(self.rockets_group) < 8:
                rockets_1 = rocket_attachment.RocketAttachment(display_width, display_height, self.alien_group)
                rockets_1.set_position(self.player.rect.left - 1, self.player.rect.y)
                self.rockets_group.add(rockets_1)

                rockets_2 = rocket_attachment.RocketAttachment(display_width, display_height, self.alien_group)
                rockets_2.set_position(self.player.rect.right - 3, self.player.rect.y)
                self.rockets_group.add(rockets_2)

                gravity = -7  # Default value is -7

                if rockets_1.vy or rockets_2.vy == 0:
                    rockets_1.vy += gravity
                    rockets_2.vy += gravity

        """ Handles events for shield creation on key press """
        if keys[pygame.K_SPACE]:
            if len(self.shield_group) > 0:
                self.shield_group.empty()
            else:
                shield = Shield(self.player, self.alien_group, self.shield_level)
                self.shield_group.add(shield)

        """ Fills the screen with a color """
        utilities.GAME_WINDOW.fill(utilities.GAME_COLORS["black"])  # Default color = Colors["majestic blue"]

        """ Draws all of the sprites on the screen and updates them """
        self.all_sprites.draw(utilities.GAME_WINDOW)
        self.all_sprites.update()

        """ Draws and updates the alien sprites """
        self.alien_group.draw(utilities.GAME_WINDOW)
        self.alien_group.update()

        """ Draws and updates the bullets """
        self.bullet_group.draw(utilities.GAME_WINDOW)
        self.bullet_group.update()

        """ Draws and updates the rockets """
        self.rockets_group.draw(utilities.GAME_WINDOW)
        self.rockets_group.update()

        """ Draws and updates the shield """
        self.shield_group.draw(utilities.GAME_WINDOW)
        self.shield_group.update()

        """ Draws the player on the  screen and updates the player """
        self.player_group.draw(utilities.GAME_WINDOW)
        self.player_group.update(self.alien_group, utilities.GAME_DELTA)

        """ Sets the title which of the window and displays info for multiple variables and objects """
        pygame.display.set_caption(
            "FPS: %.2d | all_sprites: %s | bullet_group: %s| Time played: %.2d | Remaining time: %.2d"
            % (utilities.GAME_CLOCK.get_fps(), len(self.all_sprites), len(self.bullet_group), self.time_played,
               remaining_time))
