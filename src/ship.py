import pygame

class Ship():
    """Класс для управления кораблем."""
    def __init__(self, ai_game):
        """Инициализация корабля, создание стартовой позиции"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        #* Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/space_ship.bmp')
        self.rect = self.image.get_rect()
        
        #* Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        
        #* Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)
          
        #* Флаги перемещения
        self.moving_right = False
        self.moving_left = False
        
        
    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        #* Обновляется атрибут x, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right: #* ограничение на выход за пределы правого края
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0: #* ограничение на выход за пределы левого края
            self.x -= self.settings.ship_speed
            
        #* Обновление атрибута rect на основании self.x.
        self.rect.x = round(self.x)
        
    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
        