import pygame

pygame.init()

# Fenêtre
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Bouton Pygame")

# Couleurs
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
DARK_BLUE = (0, 100, 200)

# Police pour le texte
font = pygame.font.Font(None, 36)

# Rectangle du bouton (x, y, largeur, hauteur)
button_rect = pygame.Rect(150, 120, 100, 50)

# Boucle principale
running = True
while running:
    screen.fill(WHITE)
    
    # Position de la souris
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Changer la couleur si la souris est dessus
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, DARK_BLUE, button_rect)
        if click[0]:  # clic gauche
            print("Bouton cliqué !")
    else:
        pygame.draw.rect(screen, BLUE, button_rect)

    # Texte du bouton
    text_surface = font.render("Jouer", True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
