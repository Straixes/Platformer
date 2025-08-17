import os
import pygame

class Personnage:

    def __init__(self, name, health, texturePath, width, height):
        self.name = name
        self.health = health
        self.texturePath = texturePath
        self.texture = pygame.image.load(os.path.join('img', f'{texturePath}.png'))
        self.width = width
        self.height = height

    def getWitdh(self):
        return self.width
    
    def getHeight(self):
        return self.height
