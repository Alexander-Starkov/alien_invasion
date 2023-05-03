class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        #* Размер экрана
        self.screen_width = 1200
        self.screen_height = 800
        #* Цвет фона
        self.bg_color = (66, 170, 255)
        #* Фон
        self.bg_image_path = "images/background.bmp"
        #* Настройки корабля
        self.ship_speed = 3.5
        
        #* Параметры снаряда
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,250,250)
        self.bullets_allowed = 4
  