import pygame
from mainMenu import mainMenu
class menuSelector():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0,0))  # Taille initiale
        self.running = True
        # Créer les menus
        self.menus = {
            "main": mainMenu(self.screen,self),
            
        }
        self.current_menu = "main"
    
    def changeMenu(self,name):
        self.current_menu=name
    def run(self):
        while self.running:
            mousePos = pygame.mouse.get_pos()
            mouseClick = pygame.mouse.get_pressed()
            resolution = pygame.display.get_surface().get_size()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            # Gérer et dessiner le menu 
            menu = self.menus[self.current_menu]
            menu.updateButtons(resolution,mousePos, mouseClick,False)
            pygame.display.flip()

m=menuSelector()
m.run()