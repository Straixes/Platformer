class baseMenu:
    def __init__(self, screen, menuSelect):
        self.screen = screen
        self.menuSelect = menuSelect
        self.buttons = []

    def updateButtons(self,resolution, mousePos, mouseClick,changeResolution):
        for btn in self.buttons:
            btn.update(resolution ,mousePos, mouseClick, self.screen,changeResolution)
