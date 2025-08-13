import pygame
import utilitaire
import Player
import os

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

speed = 200
gravityForce = 2450          # px/s² (valeur typique)
jumpForce = 950              # px/s (valeur typique)
playerWidth, playerHeight = 40, 100
playerPos = pygame.Vector2(300, 260)  # coin haut-gauche
groundFeetY = 360            # altitude des pieds quand on est posé
velocityY = 0

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # --- Physique / déplacement ---
    velocityY = utilitaire.deplacementPlayer(
        keys, speed, dt, playerPos, screen,
        playerWidth, playerHeight,
        gravityForce, groundFeetY,
        velocityY, jumpForce
    )

    # --- Rendu ---
    screen.fill("black")
    # sol visuel
    pygame.draw.line(screen, "white", (0, groundFeetY), (1280, groundFeetY), 2)
    # joueur
    player = Player.Player("Quentin", 100, "img/sprite.png", 209, 241)
    player.drawPlayer(screen, 360)
    pygame.display.flip()

pygame.quit()