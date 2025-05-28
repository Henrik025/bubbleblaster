import pygame #pygame library
from settings import Settings
from button import Button
from player import Player
from bubble import Bubble
from scoreboard import Scoreboard
from game_stats import GameStats
import game_functions as gf

def run_game():
    pygame.init()
    gm_settings = Settings()

    # drawing window
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)

    # set up play button
    play_button = Button(gm_settings, screen, "play")
    
    # set up the game score
    stats = GameStats()
    
    # set up scoreboard
    sb = Scoreboard(gm_settings, screen, stats)
    
    # set up clock to a decent frame rate
    clock = pygame.time.Clock()
    
    # institate player
    player = Player(screen)
    
    # institate bubble
    bubbles = pygame.sprite.Group()
    
    # run until the user asks to quit
    while True:
        gf.check_events(gm_settings, screen, player, bubbles, stats, play_button)
        if stats.game_active:
            player.update()
            gf.update_bubbles(player, bubbles, stats, sb)
            bubbles.update()
        else:
            bubbles.empty()
        gf.update_screen(gm_settings, screen, player, bubbles, clock, stats, play_button, sb)

run_game()
