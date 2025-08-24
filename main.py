from inventory.inventory import inventory
from inventory.equipment import equipment
from Menu.inventoryMenu import inventoryMenu
import pygame
from random import randint,choice
pygame.init()
screen=pygame.display.set_mode((0,0))
inv=inventory()
for i in range(54):
    inv.addEquipment(equipment("swordIcon",'accessory',randint(1,150),randint(0,1500),choice(['forged','blessed','divine','rusted','enchanted']),None,0,0,0))

class Game:
    def __init__(self):
        self.state = inventoryMenu(self,inv)
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