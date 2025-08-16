import pygame
from baseMenu import baseMenu 
import os

from assets import buttonImage,textsSettings

class settingsMenu(baseMenu):
    def __init__(self, screen,menuSelect):
        super().__init__(screen, menuSelect)
        
        #Textchangeable
        self.multiText.append(textsSettings(["12","122","325","202"],50,(0,0,0),(500,600)))
        #boutons

        self.commands.append((pygame.K_ESCAPE,self.go_to_main))

        imageSettingsRpath = os.path.join(os.path.dirname(__file__), "textureButton", "buttonSettingsRight.png")
        imageSettingsR=pygame.image.load(imageSettingsRpath).convert_alpha()
        imageSettingsRPpath = os.path.join(os.path.dirname(__file__), "textureButton", "buttonSettingsRightPressed.png")
        imageSettingsRP=pygame.image.load(imageSettingsRPpath).convert_alpha()
        imageSettingsLpath = os.path.join(os.path.dirname(__file__), "textureButton", "buttonSettingsLeft.png")
        imageSettingsL=pygame.image.load(imageSettingsLpath).convert_alpha()
        imageSettingsLPpath = os.path.join(os.path.dirname(__file__), "textureButton", "buttonSettingsLeftPressed.png")
        imageSettingsLP=pygame.image.load(imageSettingsLPpath).convert_alpha()



        self.buttons.append(buttonImage(1640, 30, 50, 50, self.multiText[0].nextText,imageSettingsR,imageSettingsRP))
        self.buttons.append(buttonImage(1440, 30, 50, 50, self.multiText[0].nextText,imageSettingsL,imageSettingsLP))

        image_path = os.path.join(os.path.dirname(__file__), "textureButton", "settings.png")
        image=pygame.image.load(image_path).convert_alpha()
        self.buttons.append(buttonImage(1840, 30, 50, 50, self.multiText[0].previousText,image,image))


    #fonction pour
    def go_to_main(self):
        self.menuSelect.changeMenu("main")
    
