import pygame
import os

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, width, height, texturePath, xCoord, yCoord):
        self.width = width
        self.height = height
        self.texturePath = texturePath
        self.texture = pygame.image.load(os.path.join('img', f'{self.texturePath}.png'))
        self.xCoord = xCoord
        self.yCoord = yCoord

        self.rect = self.texture.get_rect()

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height

    def drawObstacle(self, screen):
        screen.blit(self.texture (self.xCoord, self.yCoord))

    def getxCoord(self):
        return self.xCoord
        
    def getRect(self):
        return self.rect
    