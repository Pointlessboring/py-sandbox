class Settings:
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.fullscreen = False
        
        # Ship settings
        self.ship_limit = 3

        # Bullet setting
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # Aliens setting
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speed_up_scale = 1.1
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Fleet direction 1 represents right, -1 represents left
        self.fleet_direction = 1
    
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale

