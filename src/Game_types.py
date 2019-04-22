from math import *
import os
import sys
from Gameover_class import endgame
from BackgroundParticles_class import *
from Bullets_class import *
from AliensStream_class import *
from Rockets_class import *
from ShipShield_class import *
import pygame

# Note to self, fix player score system, collisions if needed
# Fix enemy kill system, and update system

Colors = {"red": (255, 0, 0),
          "green": (0, 255, 0),
          "blue": (0, 0, 255),
          "black": (0, 0, 0),
          "violet": (100, 0, 130),
          "majestic blue": (22, 10, 57),  # Default value = (22, 10, 57)
          "white": (255, 255, 255)}


class Res_1:

    @staticmethod
    def game_on():

        """ Method to close the game """

        def end_session():
            pygame.quit()
            sys.exit()

        """ Method which loads all pygame modules """
        pygame.init()

        """ creates a variable to hold the width and height of the screen """
        #  display_size = displaywidth, displayheight = 700, 650   # Default value for screen resolution is 900, 850
        display_size = displaywidth, displayheight = 680, 590

        os.environ['SDL_VIDEO_CENTERED'] = '1'

        """ Creates the screen with width, height, and two flags """
        window = pygame.display.set_mode(display_size, pygame.DOUBLEBUF, 32)

        """ Creates a fps counter """
        fps_logger = 68  # Default value is 53

        """ Creates a time-keeper variable """
        clock = pygame.time.Clock()

        dt = clock.tick(fps_logger)

        """ Runs and updates the amount of time played """
        time = clock.tick(fps_logger)

        """ Time counter """
        time_played = 0

        """ Amount of time game lasts """
        game_time = 121  # Default value = 201

        """ Creates an all sprites group """
        all_sprites = pygame.sprite.Group()

        """ Player group """
        player_group = pygame.sprite.Group()

        """ Bullet group """
        bullet_group = pygame.sprite.Group()

        """ Shield group """
        shield_group = pygame.sprite.Group()

        """ Aliens group """
        alien_group = pygame.sprite.Group()

        """ rocket objects group """  # Change to group which contains the AI or Aliens
        rockets_group = pygame.sprite.Group()

        """ Creates the player and gives it: a position on the screen, a 
        speed and adds to player group """

        player = Player(displaywidth, displayheight, dt, 3)
        player.set_position(displaywidth / 2, displayheight - 24)
        player_group.add(player)

        """ Creates a boolean to stop the game """
        running = True

        """ Creates a particle graphics object """
        bg_particles = BackGroundParticles()

        """ Creates a aliens stream object """
        aliens = AliensGraphics()

        """ GAME LOOP """
        """ *** NOTE TO SELF: DO NOT CREATE VARIABLES IN GAME LOOP, WILL DIMINISH FPS AND CAUSE PROBLEMS *** """
        while running:

            """ Updates/Refreshes the game fps_rate per second(s) """
            clock.tick(fps_logger)
            time_played += time / 1000.0
            remaining_time = game_time - time_played

            if len(player_group) == 0:
                endgame()

            """ Runs the particle graphics() method while the game runs """
            bg_particles.particle_graphics(displaywidth, displayheight, Colors["white"], all_sprites)

            """ Runs the alien graphics() method and limits the aliens on the screen """
            while len(alien_group) < 60:
                aliens.alien_graphics(displaywidth, displayheight, alien_group, player, player_group)

            """ Event handler """
            for event in pygame.event.get():

                """ Handles escape key event """
                if event.type == pygame.QUIT:
                    running = False
                    end_session()

                """ Handles player shoot event """
                player.reg_shot(alien_group, displayheight, bullet_group)

                """ Handles events for rocket creation """
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:

                        if len(rockets_group) > 8:
                            pass

                        else:
                            rockets_1 = RocketAttatchments(displaywidth, displayheight, alien_group)
                            rockets_1.set_position(player.rect.left - 1, player.rect.y)
                            rockets_group.add(rockets_1)

                            rockets_2 = RocketAttatchments(displaywidth, displayheight, alien_group)
                            rockets_2.set_position(player.rect.right - 3, player.rect.y)
                            rockets_group.add(rockets_2)

                            gravity = -7  # Default value is -7
                            if rockets_1.vy or rockets_2.vy == 0:
                                rockets_1.vy += gravity
                                rockets_2.vy += gravity

                """ Handles events for shield creation on key press """
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:

                        if len(shield_group) > 0:
                            shield_group.empty()

                        else:
                            shield = Shield(player, alien_group, 1)
                            shield_group.add(shield)

            """ Fills the screen with a color """
            window.fill(Colors["black"])  # Default color = Colors["majestic blue"]

            """ Draws all of the sprites on the screen and updates them """
            all_sprites.draw(window)
            all_sprites.update()

            """ Draws and updates the alien sprites """
            alien_group.draw(window)
            alien_group.update()

            """ Draws and updates the bullets """
            bullet_group.draw(window)
            bullet_group.update()

            """ Draws and updates the rockets """
            rockets_group.draw(window)
            rockets_group.update()

            """ Draws and updates the shield """
            shield_group.draw(window)
            shield_group.update()

            """ Draws the player on the  screen and updates the player """
            player_group.draw(window)
            player_group.update(alien_group, dt)

            """ Sets the title which of the window and displays info for multiple variables and objects """
            pygame.display.set_caption(
                "FPS: %.2d | all_sprites: %s | bullet_group: %s| Time played: %.2d | Remaining time: %.2d"
                % (clock.get_fps(), len(all_sprites), len(bullet_group), time_played, remaining_time))

            """ Updates/Refreshes the screen """
            pygame.display.update()


class Res_2:

    @staticmethod
    def game_on():

        """ Method to close the game """

        def end_session():
            pygame.quit()
            sys.exit()

        """ Method which loads all pygame modules """
        pygame.init()

        """ creates a variable to hold the width and height of the screen """
        display_size = displaywidth, displayheight = 700, 650

        os.environ['SDL_VIDEO_CENTERED'] = '1'

        """ Creates the screen with width, height, and two flags """
        window = pygame.display.set_mode(display_size, pygame.DOUBLEBUF, 32)

        """ Creates a fps counter """
        fps_logger = 68  # Default value is 53

        """ Creates a time-keeper variable """
        clock = pygame.time.Clock()

        dt = clock.tick(fps_logger)

        """ Runs and updates the amount of time played """
        time = clock.tick(fps_logger)

        """ Time counter """
        time_played = 0

        """ Amount of time game lasts """
        game_time = 121  # Default value = 201

        """ Creates an all sprites group """
        all_sprites = pygame.sprite.Group()

        """ Player group """
        player_group = pygame.sprite.Group()

        """ Bullet group """
        bullet_group = pygame.sprite.Group()

        """ Shield group """
        shield_group = pygame.sprite.Group()

        """ Aliens group """
        alien_group = pygame.sprite.Group()

        """ rocket objects group """  # Change to group which contains the AI or Aliens
        rockets_group = pygame.sprite.Group()

        """ Creates the player and gives it: a position on the screen, a 
        speed and adds to player group """

        player = Player(displaywidth, displayheight, dt, 1)
        player.set_position(displaywidth / 2, displayheight - 24)
        player_group.add(player)

        """ Creates a boolean to stop the game """
        running = True

        """ Creates a particle graphics object """
        bg_particles = BackGroundParticles()

        """ Creates a aliens stream object """
        aliens = AliensGraphics()

        """ GAME LOOP """
        """ *** NOTE TO SELF: DO NOT CREATE VARIABLES IN GAME LOOP, WILL DIMINISH FPS AND CAUSE PROBLEMS *** """
        while running:

            """ Updates/Refreshes the game fps_rate per second(s) """
            clock.tick(fps_logger)
            time_played += time / 1000.0
            remaining_time = game_time - time_played

            """ Runs the particle graphics() method while the game runs """
            bg_particles.particle_graphics(displaywidth, displayheight, Colors["white"], all_sprites)

            """ Runs the alien graphics() method and limits the aliens on the screen """
            while len(alien_group) < 60:
                aliens.alien_graphics(displaywidth, displayheight, alien_group, player, player_group)

            if len(player_group) == 0:
                endgame()

            """ Event handler """
            for event in pygame.event.get():

                """ Handles escape key event """
                if event.type == pygame.QUIT:
                    running = False
                    end_session()

                """ Handles player shoot event """
                player.reg_shot(alien_group, displayheight, bullet_group)

                """ Handles events for rocket creation """
                if event.type == pygame.KEYDOWN:
                    if event.key == K_DOWN:

                        if len(rockets_group) > 8:
                            pass

                        else:
                            rockets_1 = RocketAttatchments(displaywidth, displayheight, alien_group)
                            rockets_1.set_position(player.rect.left - 1, player.rect.y)
                            rockets_group.add(rockets_1)

                            rockets_2 = RocketAttatchments(displaywidth, displayheight, alien_group)
                            rockets_2.set_position(player.rect.right - 3, player.rect.y)
                            rockets_group.add(rockets_2)

                            gravity = -7  # Default value is -7
                            if rockets_1.vy or rockets_2.vy == 0:
                                rockets_1.vy += gravity
                                rockets_2.vy += gravity

                """ Handles events for shield creation on key press """
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:

                        if len(shield_group) > 0:
                            shield_group.empty()

                        else:
                            shield = Shield(player, alien_group, 1)
                            shield_group.add(shield)

            """ Fills the screen with a color """
            window.fill(Colors["black"])  # Default color = Colors["majestic blue"]

            """ Draws all of the sprites on the screen and updates them """
            all_sprites.draw(window)
            all_sprites.update()

            """ Draws and updates the alien sprites """
            alien_group.draw(window)
            alien_group.update()

            """ Draws and updates the bullets """
            bullet_group.draw(window)
            bullet_group.update()

            """ Draws and updates the rockets """
            rockets_group.draw(window)
            rockets_group.update()

            """ Draws and updates the shield """
            shield_group.draw(window)
            shield_group.update()

            """ Draws the player on the  screen and updates the player """

            player_group.draw(window)
            player_group.update(alien_group, dt)

            """ Sets the title which of the window and displays info for multiple variables and objects """
            pygame.display.set_caption(
                "FPS: %.2d | all_sprites: %s | bullet_group: %s| Time played: %.2d | Remaining time: %.2d"
                % (clock.get_fps(), len(all_sprites), len(bullet_group), time_played, remaining_time))

            """ Updates/Refreshes the screen """
            pygame.display.update()


class Res_3:

    @staticmethod
    def game_on():

        """ Method to close the game """

        def end_session():
            pygame.quit()
            sys.exit()

        """ Method which loads all pygame modules """
        pygame.init()

        os.environ['SDL_VIDEO_CENTERED'] = '1'

        """ creates a variable to hold the width and height of the screen """
        display_size = displaywidth, displayheight = 700, 650  # Default value for screen resolution is 900, 850

        """ Creates the screen with width, height, and two flags """
        window = pygame.display.set_mode(display_size, pygame.DOUBLEBUF, 32)

        """ Creates a fps counter """
        fps_logger = 78  # Default value is 53

        """ Creates a time-keeper variable """
        clock = pygame.time.Clock()

        dt = clock.tick(fps_logger)

        """ Runs and updates the amount of time played """
        time = clock.tick(fps_logger)

        """ Creates an all sprites group """
        all_sprites = pygame.sprite.Group()

        """ Player group """
        player_group = pygame.sprite.Group()

        """ Bullet group """
        bullet_group = pygame.sprite.Group()

        """ Shield group """
        shield_group = pygame.sprite.Group()

        """ Aliens group """
        alien_group = pygame.sprite.Group()

        """ rocket objects group """  # Change to group which contains the AI or Aliens
        rockets_group = pygame.sprite.Group()

        """ Creates the player and gives it: a position on the screen, a 
        speed and adds to player group """

        player = Player(displaywidth, displayheight, dt, 2)
        player.set_position(displaywidth / 2, displayheight - 24)

        player_group.add(player)

        """ Creates a boolean to stop the game """
        running = True

        """ Creates a particle graphics object """
        bg_particles = BackGroundParticles()

        """ Creates a aliens stream object """
        aliens = AliensGraphics()

        """ GAME LOOP """
        """ *** NOTE TO SELF: DO NOT CREATE VARIABLES IN GAME LOOP, WILL DIMINISH FPS AND CAUSE PROBLEMS *** """
        while running:

            """ Updates/Refreshes the game fps_rate per second(s) """
            clock.tick(fps_logger)

            """ Runs the particle graphics() method while the game runs """
            bg_particles.particle_graphics(displaywidth, displayheight, Colors["white"], all_sprites)

            """ Runs the alien graphics() method and limits the aliens on the screen """
            while len(alien_group) < 120:  # Defualt value is 60
                aliens.alien_graphics(displaywidth, displayheight, alien_group, player, player_group)

            if len(player_group) == 0:
                endgame()

            """ Event handler """
            for event in pygame.event.get():

                """ Handles escape key event """
                if event.type == pygame.QUIT:
                    running = False
                    end_session()

                """ Handles events for shield creation on key press """
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:

                        if len(shield_group) > 0:
                            shield_group.empty()

                        else:
                            shield = Shield(player, alien_group, 2)
                            shield_group.add(shield)

            """ Handles player movement """
            keys = pygame.key.get_pressed()
            if len(rockets_group) < 20:

                if keys[K_DOWN]:

                    rockets_1 = RocketAttatchments(displaywidth, displayheight, alien_group)
                    rockets_1.set_position(player.rect.left - 1, player.rect.y)
                    rockets_group.add(rockets_1)

                    rockets_2 = RocketAttatchments(displaywidth, displayheight, alien_group)
                    rockets_2.set_position(player.rect.right - 3, player.rect.y)
                    rockets_group.add(rockets_2)

                    gravity = -20  # Default value is -7
                    if rockets_1.vy or rockets_2.vy == 0:
                        rockets_1.vy += gravity
                        rockets_2.vy += gravity

            """ Fills the screen with a color """
            window.fill(Colors["black"])  # Default color = Colors["majestic blue"]

            """ Draws all of the sprites on the screen and updates them """
            all_sprites.draw(window)
            all_sprites.update()

            """ Draws and updates the alien sprites """
            alien_group.draw(window)
            alien_group.update()

            """ Draws and updates the bullets """
            bullet_group.draw(window)
            bullet_group.update()

            """ Draws and updates the rockets """
            rockets_group.draw(window)
            rockets_group.update()

            """ Draws and updates the shield """
            shield_group.draw(window)
            shield_group.update()

            """ Draws the player on the  screen and updates the player """

            player.deathray_shot(alien_group, displayheight, bullet_group)
            player_group.draw(window)
            player_group.update(alien_group, dt)

            """ Sets the title which of the window and displays info for multiple variables and objects """
            pygame.display.set_caption("FPS: %.2d " % (clock.get_fps()))

            """ Updates/Refreshes the screen """
            pygame.display.update()
