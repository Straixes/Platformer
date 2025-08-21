import pygame
import os

class Personnage(pygame.sprite.Sprite):
    def __init__(self, name, health, texturePath, width, height, xCoord, yCoord, level):
        super().__init__()
        self.name = name
        self.health = health
        self.texturePath = texturePath
        self.width = width
        self.height = height
        self.level = level

        self.texture = pygame.image.load(os.path.join('img', f'{texturePath}.png')).convert_alpha()
        self.rect = self.texture.get_rect(topleft=(xCoord, yCoord))
        self.mask = pygame.mask.from_surface(self.texture)

    # --- Getters ---
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

    # --- Vie ---
    def takeDamage(self, damage):
        self.health = max(0, self.health - damage)

    def heal(self, amount):
        self.health = min(100, self.health + amount)