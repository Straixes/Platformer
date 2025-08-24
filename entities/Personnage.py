import pygame

class Personnage(pygame.sprite.Sprite):
    def __init__(self, name, health, width, height, x, y, level):
        super().__init__()
        self.name = name
        self.health = health
        self.width = width
        self.height = height
        self.level = level

        self.rect = pygame.Rect(x, y, width, height)
        self.mask = None  # sera défini par la classe enfant

    def take_damage(self, dmg):
        self.health = max(0, self.health - dmg)

    def heal(self, amount):
        self.health = min(100, self.health + amount)
