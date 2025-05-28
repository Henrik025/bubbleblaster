import pygame #pygame library
from settings import Settings
from player import Player
import game_functions as gf

def run_game():
    pygame.init()
    gm_settings = Settings()

    # drawing window
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)

    # institate player
    player = Player(screen)
    
    # run until the user asks to quit
    while True:
        gf.check_events(player)
        player.update()
        gf.update_screen(gm_settings, screen, player)

run_game()
