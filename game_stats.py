class GameStats():
    """check the game statistics"""
    
    
    def __init__(self):
        """initialize statistics"""
        self.game_active = False
        self.reset_stats()
            
            
    def reset_stats(self):
        """initialize score, which can change during the game"""
        self.score = 0
        self.level = 1
        self.bonus = 0