import pygame

def deplacementPlayer(keys, speed, dt, player,
                      gravityForce, groundFeetY,
                      velocityY, obstacles, jumpForce=600):

    # Limites horizontales
    player.rect.x = max(0, min(player.rect.x, 1280 - player.width))

    # --- Déplacement horizontal ---
    old_rect = player.rect.copy()
    if keys[pygame.K_q]:
        player.rect.x -= speed * dt
        player.moveBackwardSprite()
    elif keys[pygame.K_d]:
        player.rect.x += speed * dt
        player.moveForwardSprite()

    # Collision horizontale pixel-perfect
    hits = pygame.sprite.spritecollide(player, obstacles, False, pygame.sprite.collide_mask)
    if hits:
        player.rect.x = old_rect.x

    # --- Calcul du bas ---
    bottom = player.rect.y + player.height

    # --- Saut ---
    if keys[pygame.K_SPACE] and bottom >= groundFeetY - 1 and velocityY == 0:
        velocityY = -jumpForce

    # --- Gravité ---
    velocityY += gravityForce * dt

    # --- Mouvement vertical ---
    old_rect = player.rect.copy()
    player.rect.y += velocityY * dt

    # Collision verticale pixel-perfect
    hits = pygame.sprite.spritecollide(player, obstacles, False, pygame.sprite.collide_mask)
    if hits:
        if velocityY > 0:  # on tombe
            player.rect.bottom = hits[0].rect.top
        elif velocityY < 0:  # on monte
            player.rect.top = hits[0].rect.bottom
        velocityY = 0

    # Collision sol
    bottom = player.rect.y + player.height
    if bottom >= groundFeetY and velocityY > 0:
        player.rect.y = groundFeetY - player.height
        velocityY = 0

    return velocityY


def drawObstacles(screen, listOfObstacles):
    for obs in listOfObstacles:
        obs.drawObstacle(screen)