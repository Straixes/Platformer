import pygame
from baseMenu import baseMenu 
import os

from assets import buttonImage,textsSettings,text,background

class settingsMenu(baseMenu):
    def __init__(self, screen, menuSelect):
        super().__init__(screen, menuSelect)
        #Textchangeable
        self.multiText=[textsSettings(["1280 x 720","1366 x 768","1600 x 900"," 1920 x 1080 "],50,(0,0,0),(1300,200)),
                        textsSettings(["fenetré","plein ecran"],50,(0,0,0),(1300,275))]
        

        defaultBackgroudPath = os.path.join(os.path.dirname(__file__), "textureBackground", "background.png")
        self.background=background(pygame.image.load(defaultBackgroudPath).convert_alpha())

        self.commands=[(pygame.K_ESCAPE,self.go_to_main)]
        #
        #image bouton
        imageSettingsRpath = os.path.join(os.path.dirname(__file__), "textureButton", "buttonSettingsRight.png")
        imageSettingsR=pygame.image.load(imageSettingsRpath).convert_alpha()
        imageSettingsRPpath = os.path.join(os.path.dirname(__file__), "textureButton", "buttonSettingsRightPressed.png")
        imageSettingsRP=pygame.image.load(imageSettingsRPpath).convert_alpha()
        imageSettingsLpath = os.path.join(os.path.dirname(__file__), "textureButton", "buttonSettingsLeft.png")
        imageSettingsL=pygame.image.load(imageSettingsLpath).convert_alpha()
        imageSettingsLPpath = os.path.join(os.path.dirname(__file__), "textureButton", "buttonSettingsLeftPressed.png")
        imageSettingsLP=pygame.image.load(imageSettingsLPpath).convert_alpha()

        #boutons resolution
        self.text.append(text("résolution",75,(0,0,0),(400,self.multiText[0].center[1])))
        self.buttons.append(buttonImage(self.multiText[0].center[0]+150, self.multiText[0].center[1]-25, 50, 50, self.multiText[0].nextText,imageSettingsR,imageSettingsRP))
        self.buttons.append(buttonImage(self.multiText[0].center[0]-200, self.multiText[0].center[1]-25, 50, 50, self.multiText[0].previousText,imageSettingsL,imageSettingsLP))

        #boutons fullscreen
        self.text.append(text("plein écran",75,(0,0,0),(400,self.multiText[1].center[1])))
        self.buttons.append(buttonImage(self.multiText[1].center[0]+150, self.multiText[1].center[1]-25, 50, 50, self.multiText[1].nextText,imageSettingsR,imageSettingsRP))
        self.buttons.append(buttonImage(self.multiText[1].center[0]-200, self.multiText[1].center[1]-25, 50, 50, self.multiText[1].previousText,imageSettingsL,imageSettingsLP))

        image_path = os.path.join(os.path.dirname(__file__), "textureButton", "settings.png")
        image=pygame.image.load(image_path).convert_alpha()
        self.buttons.append(buttonImage(1840, 30, 50, 50, self.validChange,image,image))

    #fonction pour
    def go_to_main(self):
        self.menuSelect.changeMenu("main")

    def validChange(self):
        dictResolution={"1280 x 720" : (1280,720),"1366 x 768": (1366,768),"1600 x 900": (1600,900)," 1920 x 1080 ": (1920,1080)}
        if self.multiText[1].getCurrentText()=="plein ecran":
            self.screen= pygame.display.set_mode(dictResolution[self.multiText[0].getCurrentText()], pygame.FULLSCREEN)
            self.updateSize(dictResolution[self.multiText[0].getCurrentText()])
        else:
            self.screen= pygame.display.set_mode(dictResolution[self.multiText[0].getCurrentText()])
            self.updateSize(dictResolution[self.multiText[0].getCurrentText()])




    
