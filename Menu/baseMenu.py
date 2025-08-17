import pygame
import os
class baseMenu:
    def __init__(self, screen, menuSelect):
        self.screen = screen
        self.menuSelect = menuSelect
        self.buttons = []
        self.commands = [] #forme (touche,fonction associé)
        self.text=[]
        self.multiText=[]
        self.background=None

    def updateButtons(self,resolution, mousePos, mouseClick,changeResolution):
        for btn in self.buttons:
            btn.update(resolution ,mousePos, mouseClick, self.screen,changeResolution)

    def blitTexts(self):
        for txt in self.text:
            txt.blitText(self.screen)
        for txt in self.multiText:
            txt.blitText(self.screen)

    def checkCommands(self):
        for event in pygame.event.get():
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

    def updateMenu(self,resolution, mousePos, mouseClick,changeResolution):
        self.drawBackground()
        self.updateButtons(resolution, mousePos, mouseClick,changeResolution)
        self.checkCommands()
        self.blitTexts()