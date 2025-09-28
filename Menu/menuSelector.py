import pygame
from .mainMenu import mainMenu
from .settingsMenu import settingsMenu
from .inventoryMenu import inventoryMenu
class menuSelector():
    def __init__(self,screen):
        pygame.init()
        self.screen = screen
        self.running = True
        self.menus = {
            "main": mainMenu(self.screen,self),
            "settings": settingsMenu(self.screen,self),
            
        }
        self.current_menu = "main"
    
    def changeMenu(self,name):
        self.current_menu=name
    def run(self):
        while self.running:
            mousePos = pygame.mouse.get_pos()
            mouseClick = pygame.mouse.get_pressed()
            mouseGetClicked=False

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        mouseGetClicked=True

            # Gérer et dessiner le menu 
            menu = self.menus[self.current_menu]
            menu.updateMenu(mouseClick,mouseGetClicked,mousePos,events)
            pygame.display.flip()

m=menuSelector(pygame.display.set_mode((0,0)))
m.run()