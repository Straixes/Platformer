import pygame
import sys
import pymunk
from core.code.Entities.Player import Player
from core.code.Level import Level
from core.code.Camera import CameraGroup
from core.code.Entities.Pnj import Pnj


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)

        # Espace physique
        self.space = pymunk.Space()
        self.space.gravity = (0, 1281)

        # Augmenter les itérations pour éviter le tunneling
        self.space.iterations = 30

        # Groupes
        self.camera_group = CameraGroup()

        # Niveau
        self.level = Level(self.screen, self.camera_group, self.space)

        # Joueur
        self.player = Player(self.level.spawnPoint, self.camera_group, self.space)

        # PNJ
        self.pnj1 = Pnj(self.screen, self.camera_group, "testPnj")
        self.level.addPnj(self.pnj1)

        # Associer le joueur au niveau
        self.level.setPlayer(player=self.player)

    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("#71ddee")

            # Update player (avant le step physique pour l'input)
            self.player.update(dt)

            # Step physique
            self.space.step(dt)

            # Update & draw caméra
            self.camera_group.update(dt)
            self.camera_group.customDraw(self.player)

            # Gestion PNJ dialogue
            self.level.checkPnjZones(self.player, dt, self.font)

            # Affichage FPS
            fps_text = self.font.render(f"FPS: {int(self.clock.get_fps())}", True, pygame.Color("white"))
            self.screen.blit(fps_text, (10, 10))

            pygame.display.update()