class Settings:
    """Class for game settings"""
    
    
    def __init__(self):
        """initialize game settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 139)
        self.caption = 'bubble blaster'

        self.bubble_min_r = 10
        self.bubble_max_r = 50
        
        self.bonus_score = 1000