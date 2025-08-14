class baseMenu:
    def __init__(self, screen, menuSelect):
        self.screen = screen
        self.menuSelect = menuSelect
        self.buttons = []

    def updateButtons(self,resolution, mousePos, mouseClick,changeResolution):
        for btn in self.buttons:
            btn.update(resolution ,mousePos, mouseClick, self.screen,changeResolution)

    def drawBackground(self):
        self.screen.fill((30, 30, 30))

    def updateMenu(self,resolution, mousePos, mouseClick,changeResolution):
        self.drawBackground()
        self.updateButtons(resolution, mousePos, mouseClick,changeResolution)