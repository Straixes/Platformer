import pygame
from ..baseMenu import baseMenu 
from Menu.settingsMenu.settings import saveSettings,loadSettings
from ..Assets.assets import buttonImage,MultiTexts,text,background

class settingsMenu(baseMenu):
    def __init__(self, game):
        super().__init__(game)
        #Textchangeable
        settings=loadSettings()
        def getCurrentResolutionText():
            x,y=settings["resolution"]
            textResolution=f'{x} x {y}'
            return textResolution
        def getCurrentFullScreenText():
            if settings["fullscreen"]:
                return "plein ecran"
            else:
                return "fenetré"
            
        self.multiText=[MultiTexts(["1920 x 1080","1600 x 900","1366 x 768","1280 x 720"],50,(0,0,0),(1300,200),initialText=getCurrentResolutionText()),
                        MultiTexts(["plein ecran","fenetré"],50,(0,0,0),(1300,275),initialText=getCurrentFullScreenText())]
        

        self.background=background("background.png")

        self.commands=[(pygame.K_ESCAPE,self.go_to_main)]
        #
        #image bouton

        #boutons resolution
        self.text.append(text("résolution",75,(0,0,0),(400,self.multiText[0].center[1])))
        self.buttons.append(buttonImage(self.multiText[0].center[0]+150, self.multiText[0].center[1]-25, 50, 50, self.multiText[0].nextText,"buttonSettingsRight.png","buttonSettingsRightPressed.png",True))
        self.buttons.append(buttonImage(self.multiText[0].center[0]-200, self.multiText[0].center[1]-25, 50, 50, self.multiText[0].previousText,"buttonSettingsLeft.png","buttonSettingsLeftPressed.png",True))

        #boutons fullscreen
        self.text.append(text("plein écran",75,(0,0,0),(400,self.multiText[1].center[1])))
        self.buttons.append(buttonImage(self.multiText[1].center[0]+150, self.multiText[1].center[1]-25, 50, 50, self.multiText[1].nextText,"buttonSettingsRight.png","buttonSettingsRightPressed.png",True))
        self.buttons.append(buttonImage(self.multiText[1].center[0]-200, self.multiText[1].center[1]-25, 50, 50, self.multiText[1].previousText,"buttonSettingsLeft.png","buttonSettingsLeftPressed.png",True))

        self.buttons.append(buttonImage(1840, 30, 50, 50, self.go_to_main,"settings.png","settings.png"))

        #bouton valider

        self.buttons.append(buttonImage(1700, 950, 150, 75, self.validChange,"validButton.png","validButtonPressed.png"))
        self.text.append(text("valider",35,(0,0,0),(1775,987)))

    #fonction pour
    def go_to_main(self):
        from Menu.mainMenu import mainMenu
        self.game.state=mainMenu(self.game)

    def validChange(self):
        dictResolution={"1280 x 720" : [1280,720],"1366 x 768": [1366,768],"1600 x 900": [1600,900],"1920 x 1080": [1920,1080]}
        if self.multiText[1].getCurrentText()=="plein ecran":
            self.game.screen= pygame.display.set_mode(dictResolution[self.multiText[0].getCurrentText()], pygame.FULLSCREEN)
        else:
            self.game.screen= pygame.display.set_mode(dictResolution[self.multiText[0].getCurrentText()],pygame.RESIZABLE)

            
        settings={
            "volume": 1.0,
            "resolution": dictResolution[self.multiText[0].getCurrentText()],
            "fullscreen": self.multiText[1].getCurrentText()=="plein ecran"
        }
        saveSettings(settings)




    
