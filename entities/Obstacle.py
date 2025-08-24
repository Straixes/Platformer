import pygame
import os

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, width, height, sprite_name, x, y):
        super().__init__()
        self.width = width
        self.height = height
        self.texture = pygame.image.load(os.path.join("img", f"{sprite_name}.png")).convert_alpha()
        self.rect = self.texture.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.texture)

    def draw(self, screen):
        screen.blit(self.texture, self.rect.topleft)
