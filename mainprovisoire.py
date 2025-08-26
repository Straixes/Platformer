












from inventory.inventory import inventory
from inventory.equipment import equipment
from Menu.inventoryMenu import inventoryMenu
import pygame
from random import randint,choice
pygame.init()
pygame.display.set_mode((0,0))
inv=inventory()
for i in range(55):
    inv.addEquipment(equipment("swordIcon",'sword',4,randint(0,150),choice(['forged','blessed','divine','rusted','enchanted']),None,0,0,0))
menu = inventoryMenu(pygame.display.set_mode((0,0)),inv)

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