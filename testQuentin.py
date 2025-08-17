import pygame
import utilitaire
import Player
import Obstacle

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# --- Paramètres ---
speed = 300
gravityForce = 6250         # px/s²
jumpForce = 1300              # px/s
playerWidth, playerHeight = 90, 90
playerPos = pygame.Vector2(190, 90)  # coin haut-gauche
groundFeetY = 600            # altitude des pieds quand on est posé
velocityY = 0
isRight = True

player = Player.Player("Quentin", 100, "sprite", playerWidth, playerHeight, 200, groundFeetY-playerHeight, 1)

while running:
    dt = clock.tick(60) / 1000  # delta time en secondes

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    
    # --- Physique / déplacement ---
    velocityY = utilitaire.deplacementPlayer(
        keys, speed, dt, player,
        gravityForce, groundFeetY,
        velocityY, jumpForce
    )

    # --- Rendu ---
    screen.fill("gray")
    
    # sol visuel
    pygame.draw.line(screen, "white", (0, groundFeetY), (1280, groundFeetY), 5)
    
    # joueur (position convertie en int)
    player.drawPlayer(screen)
    
    obstacle = Obstacle.Obstacle(64, 64, "obstacleTest", 360, groundFeetY-64)
    obstacle.drawObstacle(screen)

    player.isCollide(obstacle)

    pygame.display.flip()

pygame.quit()