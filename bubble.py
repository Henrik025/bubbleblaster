import pygame
import random

class Bubble(pygame.sprite.Sprite):
    """class bubble objektile"""
    
    
    def __init__(self, screen, game_settings):
        """initialize bubble"""
        super(Bubble, self).__init__()
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # bubble random radius gen
        self.bubble_radius = random.randint(game_settings.bubble_min_r, game_settings.bubble_max_r)
        # bubble surface
        self.bubble = pygame.Surface((self.bubble_radius * 2, self.bubble_radius * 2), pygame.SRCALPHA)
        # set transparency level
        self.bubble.set_alpha(120)
        # draw circle
        self.rect = pygame.draw.circle(
            self.bubble,
            (255, 255, 255),
            (self.bubble_radius, self.bubble_radius),
            self.bubble_radius,
            2)
        # surface center
        self.rect = self.bubble.get_rect(
            center=(
                random.randint(game_settings.screen_height + 20, game_settings.screen_width + 100),
                random.randint(0, game_settings.screen_height),
                )
            )
        self.speed = random.randint(1, 5)
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        
    def blit_me(self):
        self.screen.blit(self.bubble, self.rect)