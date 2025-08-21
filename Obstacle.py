import pygame
import os

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, width, height, texturePath, xCoord, yCoord):
        super().__init__()
        self.width = width
        self.height = height
        self.texturePath = texturePath
        self.texture = pygame.image.load(os.path.join('img', f'{self.texturePath}.png')).convert_alpha()

        # rect et mask pour collisions
        self.rect = self.texture.get_rect(topleft=(xCoord, yCoord))
        self.mask = pygame.mask.from_surface(self.texture)

    def drawObstacle(self, screen):
        screen.blit(self.texture, self.rect.topleft)

    def getRect(self):
        return self.rect

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getXCoord(self):
        return self.rect.x

    def getYCoord(self):
        return self.rect.y