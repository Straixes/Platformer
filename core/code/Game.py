import pygame
import sys
import pymunk
from core.code.Player import Player
from core.code.Level import Level
from core.code.Camera import CameraGroup



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

        self.space = pymunk.Space()
        self.space.gravity = (0, 500)

        # groupes
        self.camera_group = CameraGroup()

        # joueur
        self.player = Player((40, 360), self.camera_group)

        # niveau
        self.level = Level(self.screen, self.player, self.camera_group, self.space)

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
            self.level.drawShapes()

            pygame.display.update()
            self.clock.tick(60)
