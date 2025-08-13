import pygame 

class menu:
    def __init__(self):
        self.fullscreen=True
        self.resolution=(0, 0)
        self.currentMenu=0
        self.running=True
        self.screen= pygame.display.set_mode(self.resolution, pygame.FULLSCREEN)

    def runMenu(self):
        return self.running
    
    def mainMenu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.screen.fill((255, 255, 255))
        pygame.display.flip()

a=menu()

while a.running:
    a.mainMenu()