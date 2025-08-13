import pygame
import os

class Player:

    def __init__(self, name, health, texture, width, height):
        self.name = name
        self.health = health
        self.texture = texture
        self.width = width
        self.height = height
        self.image = pygame.image.load(os.path.join('img', self.texture))
    
    def drawPlayer(self, screen, position):
        screen.blit(self.image, position)

    def getSizeSprite(self):
        return (self.width, self.height)
