import pygame
import os
class baseMenu:
    def __init__(self, screen, menuSelect=None):
        self.screen = screen
        self.menuSelect = menuSelect
        self.buttons = []
        self.commands = [] #forme (touche,fonction associé)
        self.text=[]
        self.multiText=[]
        self.background=None

    def updateButtons(self,mouseClick,mouseGetClicked,mousePos):
        for btn in self.buttons:
            btn.update(self.screen,mouseClick,mouseGetClicked,mousePos)

    def blitTexts(self):
        for txt in self.text:
            txt.blitText(self.screen)
        for txt in self.multiText:
            txt.blitText(self.screen)

    def checkCommands(self,events):
        for event in events:
            for command in self.commands:
                if event.type==pygame.KEYDOWN:
                    if command[0]==event.key:
                        command[1]()

    def updateSize(self,resolution):
        for asset in self.buttons + self.text + self.multiText:
            asset.updateSize(resolution)
        self.background.updateSize(resolution)
        

    def drawBackground(self):
        self.background.blitBackground(self.screen)

    def updateMenu(self,mouseClick,mouseGetClicked,mousePos,events):
        self.drawBackground()
        self.updateButtons(mouseClick,mouseGetClicked,mousePos)
        self.checkCommands(events)
        self.blitTexts()