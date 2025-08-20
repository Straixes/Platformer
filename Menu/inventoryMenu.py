from .baseMenu import baseMenu 
import os 
from .Assets.assets import buttonImage,text,background
import pygame
class inventoryMenu(baseMenu):
    def __init__(self, screen,inventory):
        super().__init__(screen)
        self.inventory=inventory
        self.currentEquipment="sword"

        #background
        self.background=background("inventory.png")

        #boutons selection type objets
        self.buttons.append(buttonImage(960, 35, 75, 125, self.setCurrentEquipmentTo("sword"),"sword.png","swordpressed.png"))
        self.buttons.append(buttonImage(1040, 35, 75, 125, self.setCurrentEquipmentTo("shield"),"shield.png","shieldpressed.png"))
        self.buttons.append(buttonImage(1120, 35, 75, 125, self.setCurrentEquipmentTo("accessory"),"accessory.png","accessorypressed.png"))

    def setCurrentEquipmentTo(self,equipment):
        self.currentEquipment=equipment
