import pygame
from baseMenu import baseMenu 
import os

from assets import buttonImage,text
class mainMenu(baseMenu):
    def __init__(self, screen,menuSelect):
        super().__init__(screen, menuSelect)
        
        #boutons
        image_path = os.path.join(os.path.dirname(__file__), "textureButton", "settings.png")
        image=pygame.image.load(image_path).convert_alpha()
        self.buttons.append(buttonImage(1840, 30, 50, 50, self.go_to_settings,image,image))
        image_path = os.path.join(os.path.dirname(__file__), "textureButton", "play.png")
        image=pygame.image.load(image_path).convert_alpha()
        self.buttons.append(buttonImage(560, 780, 800, 120, self.go_to_settings,image,image))

        self.text.append(text("jouer",110,(0,0,0),(960,840)))

    def go_to_settings(self):
        self.menuSelect.changeMenu("settings")
