import pygame
import os

class Player:

    def __init__(self, name, health, texture, width, height):
        self.name = name
        self.health = health
        self.texture = texture
        self.width = width
        self.height = height

    
    def drawPlayer(self, screen, position):
        image = pygame.image.load(os.path.join('data', 'img/f{self.texture}'))
        screen.blit(image, position)

    def getSizeSprite(self):
        return (self.width, self.height)
