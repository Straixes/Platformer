import pygame

class menuSelector():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0,0))  # Taille initiale
        self.running = True
        # Créer les menus
        """self.menus = {
            "main": mainMenu(self.screen, self.font),
            "settings": settingsMenu(self.screen, self.font)
        }"""
        self.current_menu = "main"
    def run(self):
        return