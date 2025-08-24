import pygame

def is_on_ground_or_obstacle(player, ground_y, obstacles, margin=5):
    if player.rect.bottom >= ground_y - margin:
        return True

    for obs in obstacles:
        if player.rect.right > obs.rect.left or player.rect.left < obs.rect.right:
            if 0 <= player.rect.bottom - obs.rect.top <= margin:
                return True
    return False


def move_player(player, keys, dt, speed, gravity, jump_force, ground_y, obstacles):
    # Limites horizontales
    player.rect.x = max(0, min(player.rect.x, 1280 - player.width))

    # Déplacement horizontal
    old_x = player.rect.x
    if keys[pygame.K_q]:
        player.rect.x -= speed * dt
    elif keys[pygame.K_d]:
        player.rect.x += speed * dt

    # Collision horizontale
    hits = pygame.sprite.spritecollide(player, obstacles, False, pygame.sprite.collide_mask)
    if hits:
        player.rect.x = old_x

    # Gravité
    player.velocity_y += gravity * dt

    # Saut
    space_pressed = keys[pygame.K_SPACE]

    if space_pressed and not player.jump_pressed_last_frame and is_on_ground_or_obstacle(player, ground_y, obstacles):
        player.velocity_y = -jump_force

    player.jump_pressed_last_frame = space_pressed

    # Déplacement vertical
    player.rect.y += player.velocity_y * dt

    # Collision verticale
    hits = pygame.sprite.spritecollide(player, obstacles, False, pygame.sprite.collide_mask)
    for obs in hits:
        if player.velocity_y > 0:
            player.rect.bottom = obs.rect.top
            player.velocity_y = 0
        elif player.velocity_y < 0:
            player.rect.top = obs.rect.bottom
            player.velocity_y = 0

    # Collision sol
    if player.rect.bottom >= ground_y:
        player.rect.bottom = ground_y
        player.velocity_y = 0
