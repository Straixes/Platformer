import pygame
import os

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, width, height, texturePath, xCoord, yCoord):
        super().__init__()
        self.width = width
        self.height = height
        self.texturePath = texturePath
        self.texture = pygame.image.load(os.path.join('img', f'{self.texturePath}.png'))

        self.rect = self.texture.get_rect(topleft=(xCoord, yCoord))

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height

    def drawObstacle(self, screen):
        screen.blit(self.texture, (self.rect.x, self.rect.y))

    def getxCoord(self):
        return self.rect.x

    def getyCoord(self):
        return self.rect.y
        
    def getRect(self):
        return self.rect
    