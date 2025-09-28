import pygame
import os

class Pnj(pygame.sprite.Sprite):
    def __init__(self, screen, group, name, pos=(0,0)):
        super().__init__(group)
        self.screen = screen
        self.name = name
        self.pos = pos
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.path = os.path.join(project_root, "graphics", "pnj", f"{self.name}.png")
        self.image = pygame.image.load(self.path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)

    def setPos(self, pos):
        self.pos = pos
        self.rect.bottomleft = pos