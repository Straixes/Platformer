import pygame
import os
from Personnage import Personnage

class Player(Personnage):

    def __init__(self, name, health, texturePath, width, height):
        super().__init__(name, health, texturePath, width, height)
    
    def moveForwardSprite(self):
        self.texture = pygame.image.load(os.path.join('img', f'{self.texturePath}Forward.png'))

    def moveBackwardSprite(self):
        self.texture = pygame.image.load(os.path.join('img', f'{self.texturePath}Backward.png'))

    def jumpPlayer(self):
        self.texture = pygame.image.load(os.path.join('img', f'{self.texturePath}Jump.png'))
        
    def drawPlayer(self, screen, position):
        screen.blit(self.texture, position)

    def getSizeSprite(self):
        return (self.width, self.height)

   