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
gravityForce = 6250
jumpForce = 1400
playerWidth, playerHeight = 90, 90
groundFeetY = 600

font = pygame.font.SysFont("Arial", 24)

# Groupes
listObstacles = pygame.sprite.Group()
listPlayer = pygame.sprite.Group()

# Création obstacle et ajout une seule fois
obstacle = Obstacle.Obstacle(64, 64, "obstacleTest", 360, groundFeetY - 64)
listObstacles.add(obstacle)

# Création joueur
player = Player.Player("Quentin", 100, "sprite", playerWidth, playerHeight,
                       200, groundFeetY - playerHeight, 1, screen)
listPlayer.add(player)

# Cooldown dégâts
damage_timer = 0

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
        getattr(player, 'velocityY', 0),  # initial velocity
        listObstacles,
        jumpForce
    )
    player.velocityY = velocityY

    # --- Pixel-perfect collision et dégâts avec cooldown ---
    hits = pygame.sprite.spritecollide(player, listObstacles, False, pygame.sprite.collide_mask)
    if hits:
        player.takeDamage(15)

    # --- Rendu ---
    screen.fill((120, 120, 120))

    # FPS
    fps = int(clock.get_fps())
    fps_text = font.render(f"FPS: {fps}", True, pygame.Color("white"))
    screen.blit(fps_text, (1200, 10))

    # Sol
    pygame.draw.line(screen, (255, 255, 255), (0, groundFeetY), (1280, groundFeetY), 5)

    # Joueur
    player.drawPlayerHealthBar()
    player.drawPlayer()

    # Regénération santé (facultatif)
    if player.health < 100:
        player.heal(1)

    # Obstacles
    utilitaire.drawObstacles(screen, listObstacles)

    pygame.display.flip()

pygame.quit()