import pygame


def deplacementPlayer(keys, speed, dt, playerPos, screen,
                      playerWidth, playerHeight,
                      gravityForce, groundFeetY,
                      velocityY, jumpForce=600):

    # Limites horizontales (on clamp avec la largeur)
    if playerPos.x >= (screen.get_width() - playerWidth):
        playerPos.x = screen.get_width() - playerWidth
    if playerPos.x <= 0:
        playerPos.x = 0

    # Déplacement horizontal
    if keys[pygame.K_q]:
        playerPos.x -= speed * dt
    if keys[pygame.K_d]:
        playerPos.x += speed * dt

    # Calcul du bas du joueur (pieds)
    bottom = playerPos.y + playerHeight

    # Saut (uniquement si au sol)
    if keys[pygame.K_SPACE] and bottom >= groundFeetY - 1 and velocityY == 0:
        velocityY = -jumpForce  # impulsion vers le haut

    # Gravité
    velocityY += gravityForce * dt

    # Application du mouvement vertical
    playerPos.y += velocityY * dt

    # Recalcul des pieds après déplacement
    bottom = playerPos.y + playerHeight

    # Collision sol (seulement si on descend)
    if bottom >= groundFeetY and velocityY > 0:
        playerPos.y = groundFeetY - playerHeight
        velocityY = 0

    return velocityY
