import pygame


def jumpPlayer(playerPos, speed):
    pass
    return 0

def deplacementPlayer(keys, speed, dt, playerPos, screen):
    print(playerPos.x)
    if playerPos.x >= screen.get_size()[0] or playerPos.x <= 0:
        speed=0
    
    

    if keys[pygame.K_q]:
        playerPos.x -= speed * dt
    if keys[pygame.K_d]:
        playerPos.x += speed * dt

