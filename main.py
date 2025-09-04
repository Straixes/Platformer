import pygame
import settings
from game import Game

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Plateformer Pygame")

game = Game(screen)
game.run()

pygame.quit()
