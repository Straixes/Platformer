from .baseMenu import baseMenu 
import os 
from .Assets.assets import buttonImage,background,image
import pygame
class inventoryMenu(baseMenu):
    def __init__(self, screen,inventory):
        super().__init__(screen)
        self.inventory=inventory
        self.inventory.sortEquipment("sword",lambda x : x.level,True)
        self.currentEquipment="sword"

        #background
        self.background=background("inventory.png")

        #boutons selection type objets
        self.buttons.append(buttonImage(960, 30, 75, 125, self.setCurrentEquipmentToSword,"sword.png","swordpressed.png"))
        self.buttons.append(buttonImage(1040, 30, 75, 125, self.setCurrentEquipmentToShield,"shield.png","shieldpressed.png"))
        self.buttons.append(buttonImage(1120, 30, 75, 125, self.setCurrentEquipmentToAccessory,"accessory.png","accessorypressed.png"))

        self.buttons.append(buttonImage(1835, 160, 50, 50, self.inventory.decreaseLign,"up.png","upPressed.png"))
        self.buttons.append(buttonImage(1835, 980, 50, 50,  self.inventory.increaseLign,"down.png","downPressed.png"))

        self.image.append(image(265,305,160,160,"swordIcon.png",self.inventory.isSlotSwordEmpty))
        self.image.append(image(265,530,160,160,"shieldIcon.png",self.inventory.isSlotShieldEmpty))
        self.image.append(image(265,755,160,160,"swordIcon.png",self.inventory.isSlotSwordEmpty))
        self.image.append(image(510,305,160,160,"accessoryIcon.png",self.inventory.isSlotAccessory1Empty))
        self.image.append(image(510,530,160,160,"accessoryIcon.png",self.inventory.isSlotAccessory2Empty))
        self.image.append(image(510,755,160,160,"accessoryIcon.png",self.inventory.isSlotAccessory3Empty))

        self.image.append(image(960, 30, 75, 125,"swordpressed.png",self.isCurrentEquipmentSword))
        self.image.append(image(1040, 30, 75, 125,"shieldpressed.png",self.isCurrentEquipmentShield))
        self.image.append(image(1120, 30, 75, 125,"accessorypressed.png",self.isCurrentEquipmentAccessory))

        self.additionalFonction.append(self.inventory.fonctionDrawEquipment(self.screen))



    def isCurrentEquipmentSword(self):
        return self.currentEquipment=='sword'
    def isCurrentEquipmentShield(self):
        return self.currentEquipment=='shield'
    def isCurrentEquipmentAccessory(self):
        return self.currentEquipment=='accessory'
    
    def setCurrentEquipmentToSword(self):
        self.inventory.sortEquipment("sword",lambda x : x.level,True)
        self.currentEquipment="sword"
    def setCurrentEquipmentToShield(self):
        self.inventory.sortEquipment("shield",lambda x : x.level,True)
        self.currentEquipment="shield"
    def setCurrentEquipmentToAccessory(self):
        self.inventory.sortEquipment("accessory",lambda x : x.level,True)
        self.currentEquipment="accessory"
