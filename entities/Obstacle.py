import pygame
import os

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, sprite_name, x, y):
        super().__init__()

        # Chargement et redimensionnement de l'image
        texture_path = os.path.join("img", f"{sprite_name}.png")
        self.texture = pygame.image.load(texture_path).convert_alpha()
        self.width = self.texture.get_width()
        self.height = self.texture.get_height()

        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

        # Rectangle et masque de collision
        self.rect = self.texture.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.texture)

    def draw(self, screen):
        screen.blit(self.texture, self.rect.topleft)
