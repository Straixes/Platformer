import pygame

import settings
from entities import Plateform

def is_on_ground_or_obstacle(player, ground_y, obstacles, margin=0):
    if player.rect.bottom >= ground_y - margin:
        return True

    for obs in obstacles:
        if player.rect.right >= obs.rect.left or player.rect.left <= obs.rect.right:
            if 0 <= player.rect.bottom - obs.rect.top <= margin:
                return True
    return False


def move_player(player, keys, dt, speed, gravity, jump_force, ground_y, obstacles):
    # Déplacement horizontal
    old_x = player.rect.x
    if keys[pygame.K_q]:
        player.rect.x -= speed * dt
    elif keys[pygame.K_d]:
        player.rect.x += speed * dt

    # Collision horizontale
    hits = pygame.sprite.spritecollide(player, obstacles, False, pygame.sprite.collide_mask)

    # Gravité
    player.velocity_y += gravity * dt

    # Saut
    space_pressed = keys[pygame.K_SPACE]
    if space_pressed and not player.jump_pressed_last_frame and is_on_ground_or_obstacle(player, ground_y, obstacles):
        player.velocity_y = -jump_force
    player.jump_pressed_last_frame = space_pressed

    # Déplacement vertical
    player.rect.y += player.velocity_y * dt

    hits = pygame.sprite.spritecollide(player, obstacles, False, pygame.sprite.collide_mask)

    for obs in hits:
        # --- Joueur tombe sur un obstacle ---
        if player.velocity_y > 0 and player.rect.bottom <= obs.rect.top + obs.rect.width/5:
            player.rect.bottom = obs.rect.top
            player.velocity_y = 0

            # Transport si plateforme mouvante
            if isinstance(obs, Plateform):
                player.rect.x += obs.velocity * obs.direction

        # --- Joueur cogne par dessous ---
        elif player.velocity_y < 0 and player.rect.top >= obs.rect.bottom - obs.rect.width/5:
            player.rect.top = obs.rect.bottom
            player.velocity_y = 0

        # --- Joueur touche sur le côté ---
        else:
            if isinstance(obs, Plateform):
                # La plateforme change de direction si on la percute
                obs.direction *= -1
                obs.distance_traveled = 0  # reset pour éviter un demi-tour instantané
            # On bloque le joueur pour éviter de passer à travers
            if player.rect.centerx < obs.rect.centerx:
                player.rect.right = obs.rect.left
            else:
                player.rect.left = obs.rect.right

    # Collision avec le sol
    if player.rect.bottom > ground_y:
        player.rect.bottom = ground_y
        player.velocity_y = 0

