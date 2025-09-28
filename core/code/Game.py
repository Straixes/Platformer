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

        self.space = pymunk.Space()
        self.space.gravity = (0, 981)

        # groupes
        self.camera_group = CameraGroup()

        # niveau
        self.level = Level(self.screen, self.camera_group, self.space)

        # joueur
        self.player = Player(self.level.spawnPoint, self.camera_group, self.space)

        # Pnj
        self.pnj1 = Pnj(self.screen, self.camera_group, 'testPnj')
        self.level.addPnj(self.pnj1)

        self.level.setPlayer(player=self.player)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('#71ddee')  # nettoie l’écran

            self.level.space.step(1/50)

            # update player avec collisions
            self.player.update()

            # update et draw
            self.camera_group.update()
            self.camera_group.customDraw(self.player)

            self.screen.blit(self.font.render(f"FPS: {int(self.clock.get_fps())}", True, pygame.Color("white")), (10, 10))

            pygame.display.update()
            self.clock.tick(60)
