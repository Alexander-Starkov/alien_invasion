import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, с одним пришельцем"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        
        #* Загрузка изображения пришельца и назначения стартовой позиции через атрибут rect
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()
        
        #* Появление пришельцев в верхнем левом углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #* Сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)
        
        
        