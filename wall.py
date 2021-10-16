import pygame


class Wall(pygame.sprite.Sprite):
    x = 0
    y = 0
    moving = True

    def __init__(self, width, height, pos_x, pos_y, color, moving):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.x = pos_x
        self.y = pos_y