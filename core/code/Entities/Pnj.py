import pygame
import os

class Pnj(pygame.sprite.Sprite):
    def __init__(self, screen, group, name, pos=(0,0)):
        super().__init__(group)
        self.screen = screen
        self.name = name
        self.pos = pos
        self.project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.path = os.path.join(self.project_root, "graphics", "pnj", f"{self.name}.png")
        self.image = pygame.image.load(self.path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)

        # Variables de dialogue
        self.index_ligne = 0
        self.timer = 0
        self.delai = 1000  # ms entre les lignes
        self.lignes = None  # sera chargée seulement si besoin

    def setPos(self, pos):
        self.pos = pos
        self.rect.bottomleft = pos

    def onPlayerNearby(self, dt, font):
        # Charger le fichier une seule fois
        if self.lignes is None:
            path = os.path.abspath(os.path.join(self.project_root, "..", "pnjDialogs", f"{self.name}Dialog.txt"))
            with open(path, "r", encoding="utf-8") as f:
                self.lignes = [l.strip() for l in f]

        # Mise à jour du timer
        self.timer += dt * 1000  # dt est en secondes, on veut ms

        if self.index_ligne < len(self.lignes) - 1 and self.timer >= self.delai:
            self.index_ligne += 1
            self.timer = 0

        # Afficher la ligne courante
        text_surf = font.render(self.lignes[self.index_ligne], True, (255, 255, 255))
        self.screen.blit(text_surf, (self.pos[0]+300, self.pos[1]+15))