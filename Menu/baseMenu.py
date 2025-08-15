import pygame
class baseMenu:
    def __init__(self, screen, menuSelect):
        self.screen = screen
        self.menuSelect = menuSelect
        self.buttons = []
        self.commands = [] #forme (touche,fonction associé)
        self.text=[]

    def updateButtons(self,resolution, mousePos, mouseClick,changeResolution):
        for btn in self.buttons:
            btn.update(resolution ,mousePos, mouseClick, self.screen,changeResolution)

    def blitTexts(self):
        for txt in self.text:
            txt.blitText(self.screen)

    def checkCommands(self):
        for event in pygame.event.get():
            for command in self.commands:
                if event.type==pygame.KEYDOWN:
                    if command[0]==event.key:
                        command[1]()

    def drawBackground(self):
        self.screen.fill((30, 30, 30))

    def updateMenu(self,resolution, mousePos, mouseClick,changeResolution):
        self.drawBackground()
        self.updateButtons(resolution, mousePos, mouseClick,changeResolution)
        self.checkCommands()
        self.blitTexts()