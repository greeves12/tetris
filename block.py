import pygame

class Block(pygame.sprite.Sprite):
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
        self.moving = moving

    def update(self, new_x, new_y):
        self.x += new_x
        self.y += new_y
        self.rect.center = [self.x, self.y]

    def finish(self):
        self.moving = False

    def get_status(self):
        return self.moving

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

