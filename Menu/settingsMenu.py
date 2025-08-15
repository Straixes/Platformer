import pygame
from baseMenu import baseMenu 
import os

from button import buttonImage

class settingsMenu(baseMenu):
    def __init__(self, screen,menuSelect):
        super().__init__(screen, menuSelect)
        
        #boutons
        image_path = os.path.join(os.path.dirname(__file__), "textureButton", "settings.jpg")
        image=pygame.image.load(image_path).convert_alpha()
        self.buttons.append(buttonImage(10, 120, 25, 25, self.go_to_main,image,image))

        self.commands.append((pygame.K_ESCAPE,self.go_to_main))

    def go_to_main(self):
        self.menuSelect.changeMenu("main")
