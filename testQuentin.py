import pygame
import utilitaire

# pygame setupdddd
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
speed = 200
gravityForce = 100
velocityY=0
dt = 0

playerPos = pygame.Vector2(300, 360)

while running:
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.rect(screen, "blue", (800, 340, 20, 50), 30)

    pygame.draw.circle(screen, "red", (playerPos.x - 250, playerPos.y), 40)    

    player = pygame.Rect(playerPos.x, playerPos.y, 40, 100)
    pygame.draw.rect(screen, "red", player, 100)


    keys = pygame.key.get_pressed()
    if keys:
        utilitaire.deplacementPlayer(keys, speed, dt, playerPos, screen, 40, gravityForce, 360, velocityY)

    # flip() the display to put your work on screen
    pygame.display.flip()



pygame.quit()


