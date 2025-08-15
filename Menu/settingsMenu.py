import pygame
from baseMenu import baseMenu 
import os

from assets import buttonImage

class settingsMenu(baseMenu):
    def __init__(self, screen,menuSelect):
        super().__init__(screen, menuSelect)
        
        #boutons

        self.commands.append((pygame.K_ESCAPE,self.go_to_main))


    #fonction pour
    def go_to_main(self):
        self.menuSelect.changeMenu("main")
    
