import pygame
import os
from Personnage import Personnage

class Player(Personnage):
    def __init__(self, name, health, texturePath, width, height, xCoord, yCoord, level, screen):
        super().__init__(name, health, texturePath, width, height, xCoord, yCoord, level)
        self.screen = screen

        # Chargement de tous les sprites
        self.sprites = {
            "idle": pygame.image.load(os.path.join('img', f"{self.texturePath}.png")).convert_alpha(),
            "forward": pygame.image.load(os.path.join('img', f"{self.texturePath}Forward.png")).convert_alpha(),
            "backward": pygame.image.load(os.path.join('img', f"{self.texturePath}Backward.png")).convert_alpha(),
            "jump": pygame.image.load(os.path.join('img', f"{self.texturePath}RightJump.png")).convert_alpha()
        }
        self.texture = self.sprites["idle"]
        self.mask = pygame.mask.from_surface(self.texture)

    # --- Changement de sprite ---
    def moveForwardSprite(self):
        self.texture = self.sprites["forward"]
        self.mask = pygame.mask.from_surface(self.texture)

    def moveBackwardSprite(self):
        self.texture = self.sprites["backward"]
        self.mask = pygame.mask.from_surface(self.texture)

    def jumpPlayer(self):
        self.texture = self.sprites["jump"]
        self.mask = pygame.mask.from_surface(self.texture)

    # --- Dessin ---
    def drawPlayer(self):
        self.screen.blit(self.texture, self.rect.topleft)

    def drawPlayerHealthBar(self):
        # Fond rouge
        pygame.draw.rect(self.screen, (200,0,0), (10, 10, 200, 20))
        # Barre verte proportionnelle
        pygame.draw.rect(self.screen, (0,200,0), (10, 10, (self.health/100)*200, 20))