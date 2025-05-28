import pygame

class Player(pygame.sprite.Sprite):
    """player objecti klass"""
    
    
    def __init__(self, screen):
    
        super(Player, self).__init__()
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.player = pygame.Surface((75, 25))
        self.player.fill((255, 0, 0))
        self.rect = self.player.get_rect()
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        if self.moving_right:
            self.rect.move_ip(5, 0)
        if self.moving_left:
            self.rect.move_ip(-5, 0)
        if self.moving_up:
            self.rect.move_ip(0, -5)
        if self.moving_down:
            self.rect.move_ip(0, 5)
        
    def blit_me(self):
        self.screen.blit(self.player, self.rect)