class baseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = None
        self.buttons = []

    def updateButtons(self, mousePos, mouseClick):
        for btn in self.buttons:
            btn.update(mousePos, mouseClick, self.screen)

    def draw(self):
        self.screen.fill((255, 255, 255)) # à changer pour image ou fond meme si image preferable
        for btn in self.buttons:
            btn.draw(self.screen)