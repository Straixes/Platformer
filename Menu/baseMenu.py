import pygame
from state import State
from Menu.Assets.assets import getMousePos
class baseMenu(State):
    def __init__(self,game):
        super().__init__(game)
        self.buttons = []
        self.commands = [] #forme (touche,fonction associé)
        self.text=[]
        self.multiText=[]
        self.image=[]
        self.additionalFonction=[]
        self.background=None

    def updateButtonsEvents(self,events,ScreenInfo):
        mousePos = getMousePos(ScreenInfo)
        mouseClick = pygame.mouse.get_pressed()
        mouseGetClicked = False
        
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:  
                mouseGetClicked = True
        for btn in self.buttons:
            btn.update(mouseClick,mouseGetClicked,mousePos)
    
    def drawButtons(self,screen,ScreenInfo):
        mouse_pos = getMousePos(ScreenInfo)
        for btn in self.buttons:
            btn.draw(screen,mouse_pos)

    def blitTexts(self,screen):
        for txt in self.text:
            txt.blitText(screen)
        for txt in self.multiText:
            txt.blitText(screen)

    def blitImage(self,screen):
        for img in self.image:
            img.update(screen)

    def checkCommands(self,events):
        for event in events:
            for command in self.commands:
                if event.type==pygame.KEYDOWN:
                    if command[0]==event.key:
                        command[1]()

    def updateSize(self,resolution):
        for asset in self.buttons + self.text + self.multiText +self.image:
            asset.updateSize(resolution)
        self.background.updateSize(resolution)

    def checkAdditionalFonction(self):
        for fn in self.additionalFonction:
            fn()   

    def drawBackground(self,screen):
        self.background.blitBackground(screen)

    def update(self,ScreenInfo):
        self.checkAdditionalFonction
    
    def handle_events(self, events,ScreenInfo):
        self.checkCommands(events)
        self.updateButtonsEvents(events,ScreenInfo)
    
    def draw(self, screen,ScreenInfo):
        self.drawBackground(screen)
        self.blitImage(screen)
        self.drawButtons(screen,ScreenInfo)
        self.blitTexts(screen)