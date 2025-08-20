from inventory.inventory import inventory
from Menu.inventoryMenu import inventoryMenu
import pygame

menu = inventoryMenu(pygame.display.set_mode((0,0)),inventory())

run=True
while run:
    mousePos = pygame.mouse.get_pos()
    mouseClick = pygame.mouse.get_pressed()
    mouseGetClicked=False

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
           run = False
           if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                mouseGetClicked=True

    # Gérer et dessiner le menu 

    menu.updateMenu(mouseClick,mouseGetClicked,mousePos,events)
    pygame.display.flip()