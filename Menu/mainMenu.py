import pygame
from baseMenu import baseMenu 
import os

from button import buttonImage
class mainMenu(baseMenu):
    def __init__(self, screen,menuSelect):
        super().__init__(screen, menuSelect)
        
        #boutons
        image_path = os.path.join(os.path.dirname(__file__), "textureButton", "settings.jpg")
        image=pygame.image.load(image_path).convert_alpha()
        self.buttons.append(buttonImage(10, 10, 25, 25, self.go_to_settings,image,image))

    def go_to_settings(self):
        self.menuSelect.changeMenu("settings")
