import pygame 
from button import buttonText

pygame.init()
class menu:
    def __init__(self):
        self.fullscreen=False
        self.resolution=(0, 0)
        self.currentMenu=0
        self.running=True
        self.changeResolution=True

        if self.fullscreen:
            self.screen= pygame.display.set_mode(self.resolution, pygame.FULLSCREEN)
        else:
            self.screen= pygame.display.set_mode(self.resolution)

        #mainMenu
        self.font=pygame.font.Font(None, 36)
        self.buttonMainMenuSettings=buttonText(10,10,100,100,None,"S",(1,2,50),(152,20,20),(152,200,20),self.font)

    def runMenu(self):
        return self.running
    
    def mainMenu(self):
        #souris
        mousePos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        resolution=pygame.display.get_surface().get_size()
        
        self.screen.fill((255, 255, 255))
        self.buttonMainMenuSettings.update(resolution,mousePos,click,self.screen,self.changeResolution)

        if self.changeResolution:
            self.changeResolution=False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        pygame.display.flip()

a=menu()

while a.running:
    a.mainMenu()