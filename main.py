
from Menu.mainMenu import mainMenu
import pygame
from Menu.settingsMenu.settings import loadSettings
pygame.init()

settings=loadSettings()
screen=pygame.display.set_mode((0,0))
class Game:
    def __init__(self):
        self.state = mainMenu(self)
        self.logicalSurface=pygame.Surface((1920, 1080))
        if settings["fullscreen"]==True:
            self.screen= pygame.display.set_mode(settings['resolution'], pygame.FULLSCREEN)
        else:
            self.screen= pygame.display.set_mode(settings['resolution'], pygame.RESIZABLE)
        
        


    def change_state(self, state):
        self.state = state
    
    def run(self):
        run=True
        while run:
        
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    run=False
            self.state.handle_events(events)
            self.state.update()
            self.state.draw(self.logicalSurface)
            
            window_width, window_height = self.screen.get_size()
            scale_x = window_width / 1920
            scale_y = window_height / 1080
            scale = min(scale_x, scale_y)

            scaled_width = int(1920 * scale)
            scaled_height = int(1080 * scale)

            offset_x = (window_width - scaled_width) // 2
            offset_y = (window_height - scaled_height) // 2

            self.screen.fill((0, 0, 0))
            
            screen.blit(pygame.transform.scale(self.logicalSurface, (scaled_width,scaled_height)),(offset_x, offset_y))
            pygame.display.flip()

game=Game()
game.run()
