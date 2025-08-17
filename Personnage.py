import os
import pygame
from Obstacle import Obstacle

class Personnage(pygame.sprite.Sprite):

    def __init__(self, name, health, texturePath, width, height, xCoord, yCoord, level):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.health = health
        self.texturePath = texturePath
        self.texture = pygame.image.load(os.path.join('img', f'{texturePath}.png'))
        self.width = width
        self.height = height
        self.level = level

        self.rect = self.texture.get_rect(topleft=(xCoord, yCoord))

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getRect(self):
        return self.rect

    def getXCoord(self):
        return self.rect.x

    def getYCoord(self):
        return self.rect.y
    
    def isCollide(self, collider):
        assert isinstance(collider, (Obstacle, Personnage)), "Ce n'est pas un personnage."
        if self.rect.colliderect(collider.rect):
            print("1")
        else:
            print("2")
