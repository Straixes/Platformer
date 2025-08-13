import pygame
import utilitaire
import Player

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# --- Paramètres ---
speed = 200
gravityForce = 8500          # px/s²
jumpForce = 1800              # px/s
playerWidth, playerHeight = 40, 100
playerPos = pygame.Vector2(300, 260)  # coin haut-gauche
groundFeetY = 360            # altitude des pieds quand on est posé
velocityY = 0

# --- Création du joueur (une seule fois) ---
player = Player.Player("Quentin", 100, "sprite.png", playerWidth, playerHeight)

while running:
    dt = clock.tick(60) / 1000  # delta time en secondes

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
    
    # joueur (position convertie en int)
    player.drawPlayer(screen, (int(playerPos.x), int(playerPos.y)))
    
    pygame.display.flip()

pygame.quit()