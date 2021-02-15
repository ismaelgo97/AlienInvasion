class Settings:

    def __init__(self):
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #Ship settings
        self.ship_speed = 1.5
        #Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60 ,60)
        self.bullets_allowed = 3
        #alien settings
        self.alien_speed = 1.0
        self.alien_drop = 10
        self.alien_direction = 1 #1 right, -1 left

