import pygame
import os

class Player:

    def __init__(self, name, health, texture, width, height):
        self.name = name
        self.health = health
        self.texture = texture
        self.width = width
        self.height = height
        self.image = pygame.image.load(os.path.join('img', f'{self.texture}.png'))
        self.numberForMove = 0
    
    def moveForwardSprite(self):
        self.image = pygame.image.load(os.path.join('img', f'{self.texture}Forward.png'))

    def moveBackwardSprite(self):
        self.image = pygame.image.load(os.path.join('img', f'{self.texture}Backward.png'))

    def jumpPlayer(self):
        self.image = pygame.image.load(os.path.join('img', f'{self.texture}Jump.png'))
        

    def drawPlayer(self, screen, position):
        screen.blit(self.image, position)

    def getSizeSprite(self):
        return (self.width, self.height)

   