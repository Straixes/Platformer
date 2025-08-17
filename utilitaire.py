import pygame


def deplacementPlayer(keys, speed, dt, player,
                      gravityForce, groundFeetY,
                      velocityY, jumpForce=600):
    # Limites horizontales
    if player.rect.x >= (1280 - player.width):  # ou screen.get_width()
        player.rect.x = 1280 - player.width
    if player.rect.x <= 0:
        player.rect.x = 0

    # Déplacement horizontal
    if keys[pygame.K_q]:
        player.rect.x -= speed * dt
        player.moveBackwardSprite()
    elif keys[pygame.K_d]:
        player.rect.x += speed * dt
        player.moveForwardSprite()

    # Calcul du bas du joueur
    bottom = player.rect.y + player.height

    # Saut
    if keys[pygame.K_SPACE] and bottom >= groundFeetY - 1 and velocityY == 0:
        velocityY = -jumpForce

    # Gravité
    velocityY += gravityForce * dt

    # Mouvement vertical
    player.rect.y += velocityY * dt

    # Collision avec le sol
    bottom = player.rect.y + player.height
    if bottom >= groundFeetY and velocityY > 0:
        player.rect.y = groundFeetY - player.height
        velocityY = 0

    return velocityY
