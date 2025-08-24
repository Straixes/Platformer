import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from game import Game

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plateformer Pygame")

game = Game(screen)
game.run()

pygame.quit()
