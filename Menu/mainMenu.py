
from .baseMenu import baseMenu 

from .Assets.assets import buttonImage,text,background
class mainMenu(baseMenu):
    def __init__(self, game):
        super().__init__(game)
        
        self.background=background("background.png")
        #boutons
        self.buttons.append(buttonImage(1840, 30, 50, 50, self.go_to_settings,"settings.png","settings.png"))
        self.buttons.append(buttonImage(560, 780, 800, 120, self.go_to_settings,"play.png","playButtonPressed.png"))


        self.text.append(text("jouer",110,(0,0,0),(960,840)))

    def go_to_settings(self):
        from .settingsMenu import settingsMenu
        self.game.state=settingsMenu(self.game)
