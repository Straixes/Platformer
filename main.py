from inventory.inventory import inventory
from inventory.equipment import equipment
from Menu.mainMenu import mainMenu
import pygame

pygame.init()
screen=pygame.display.set_mode((0,0))

class Game:
    def __init__(self):
        self.state = mainMenu(self)
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
            self.state.draw(screen)
            pygame.display.flip()

game=Game()
game.run()