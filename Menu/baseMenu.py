import pygame
class baseMenu:
    def __init__(self, screen, menuSelect):
        self.screen = screen
        self.menuSelect = menuSelect
        self.buttons = []
        self.commands = [] #forme (touche,fonction associé)
        self.text=[]
        self.multiText=[]

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

    def drawBackground(self):
        self.screen.fill((150, 150, 150))

    def updateMenu(self,resolution, mousePos, mouseClick,changeResolution):
        self.drawBackground()
        self.updateButtons(resolution, mousePos, mouseClick,changeResolution)
        self.checkCommands()
        self.blitTexts()