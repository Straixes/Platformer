import pygame


def deplacementPlayer(keys, speed, dt, playerPos, screen, playerSize, gravityForce, groundY, velocityY, jumpForce=500):
    # Limites écran
    if playerPos.x >= (screen.get_size()[0] - playerSize):
        playerPos.x = screen.get_size()[0] - playerSize
    if playerPos.x <= 0:
        playerPos.x = 0

    # Déplacement horizontal
    if keys[pygame.K_q]:
        playerPos.x -= speed * dt
    if keys[pygame.K_d]:
        playerPos.x += speed * dt

    # Saut (seulement si sur le sol)
    if keys[pygame.K_SPACE] and playerPos.y >= groundY:
        velocityY = -jumpForce

    # Gravité
    velocityY += gravityForce * dt
    playerPos.y += velocityY * dt

    # Collision sol
    if playerPos.y >= groundY:
        playerPos.y = groundY
        velocityY = 0

    return velocityY
