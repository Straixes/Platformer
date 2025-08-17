import pygame
import os

class Obstacle:
    def __init__(self, width, height, texturePath):
        self.width = width
        self.height = height
        self.texturePath = texturePath
        self.texture = pygame.image.load(os.path.join('img', f'{self.texturePath}.png'))

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height

    def drawObstacle(self, screen, position):
        screen.blit(self.texture, position)
        

    def isCollide(self, personnage):
        if pygame.Rect.colliderect(self.rect()):
            print("AHHHHHHHHH")