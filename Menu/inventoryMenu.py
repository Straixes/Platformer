from state import State 
from .Assets.assets import buttonImage,background,image
import pygame
import math
class inventoryMenu(State):
    def __init__(self,game,inventory):
        super().__init__(game)
        self.inventory=inventory
        self.inventory.sortEquipment("sword",lambda x : x.level,True)
        self.currentEquipment="sword"

        #background
        self.background=background("inventory.png")

        #boutons selection type objets
        self.buttons=[
            buttonImage(960, 30, 75, 125, self.setCurrentEquipmentToSword,"sword.png","swordpressed.png"),
            buttonImage(1040, 30, 75, 125, self.setCurrentEquipmentToShield,"shield.png","shieldpressed.png"),
            buttonImage(1120, 30, 75, 125, self.setCurrentEquipmentToAccessory,"accessory.png","accessorypressed.png"),
            buttonImage(1835, 160, 50, 50, self.inventory.decreaseLign,"up.png","upPressed.png"),
            buttonImage(1835, 980, 50, 50,  self.inventory.increaseLign,"down.png","downPressed.png")]
        self.images= [
            image(265,305,160,160,"swordIcon.png",self.inventory.isSlotSwordEmpty),
            image(265,530,160,160,"shieldIcon.png",self.inventory.isSlotShieldEmpty),
            image(265,755,160,160,"swordIcon.png",self.inventory.isSlotSwordEmpty),
            image(510,305,160,160,"accessoryIcon.png",self.inventory.isSlotAccessory1Empty),
            image(510,530,160,160,"accessoryIcon.png",self.inventory.isSlotAccessory2Empty),
            image(510,755,160,160,"accessoryIcon.png",self.inventory.isSlotAccessory3Empty),

            image(960, 30, 75, 125,"swordpressed.png",self.isCurrentEquipmentSword),
            image(1040, 30, 75, 125,"shieldpressed.png",self.isCurrentEquipmentShield),
            image(1120, 30, 75, 125,"accessorypressed.png",self.isCurrentEquipmentAccessory)]
        self.dictPosSlot={
            "sword": (265,305),
            "shield": (265,530),
            "accessory1": (510,305),
            "accessory2": (510,530),
            "accessory3": (510,755)
        }
        self.scrollRect=pygame.Rect(960,160,870,870)
        self.selectingAccessory=False
        self.selectedEquipment=None

        self.rectSlotAccessory1=pygame.Rect(505,300,170,170)
        self.rectSlotAccessory2=pygame.Rect(505,525,170,170)
        self.rectSlotAccessory3=pygame.Rect(505,750,170,170)

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
    #######DRAW#######
    def drawEquipments(self,screen):
            lenList=len(self.inventory.currentDrawlist)
            for i in range(lenList):
                self.inventory.currentDrawlist[i].draw(screen,965+175*(i%5),165+175*(i//5))

    def drawBackground(self,screen):
        self.background.blitBackground(screen)
    
    def drawButtons(self,screen):
        mouse_pos = pygame.mouse.get_pos()
        for btn in self.buttons:
            btn.draw(screen,mouse_pos)

    def drawEquipedEquipments(self,screen):
        for key in self.inventory.dictSlot.keys():
            equipment=self.inventory.dictSlot[key]
            if equipment !=None:
                x,y=self.dictPosSlot[key]
                equipment.draw(screen,x,y)

    def draw_blinking_border(self, screen, rect, base_color=(255, 255, 255), thickness=4, speed=0.0025):
        time = pygame.time.get_ticks()
        alpha = (math.sin(time * speed) +2) / 4  # oscillation entre 0 et 1
        color = (int(base_color[0] * alpha), int(base_color[1] * alpha), int(base_color[2] * alpha))
        pygame.draw.rect(screen, color, rect, thickness)

    def blitImage(self,screen):
        for img in self.images:
            img.update(screen)
    
    def draw(self, screen):
        self.drawBackground(screen)
        self.drawButtons(screen)
        self.blitImage(screen)
        self.drawEquipments(screen)
        self.drawEquipedEquipments(screen)

        if self.selectingAccessory:
            self.draw_blinking_border(screen, self.rectSlotAccessory1)
            self.draw_blinking_border(screen, self.rectSlotAccessory2)
            self.draw_blinking_border(screen, self.rectSlotAccessory3)

    ### handle events########
    def updateButtonsEvents(self,events):
        mousePos = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()
        mouseGetClicked = False
        
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:  
                mouseGetClicked = True
        for btn in self.buttons:
            btn.update(mouseClick,mouseGetClicked,mousePos)

    def scrollInventory(self,events):
        mousePos = pygame.mouse.get_pos()
        if self.scrollRect.collidepoint(mousePos):

            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.inventory.decreaseLign()
                    elif event.button == 5:
                        self.inventory.increaseLign()
    
    def buttonEquipment(self,events):
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.scrollRect.collidepoint(mousePos):
                    lenList=len(self.inventory.currentDrawlist)
                    for i in range(lenList):
                        rectEquipment=pygame.Rect(960+175*(i%5),160+175*(i//5),170,170)
                        if rectEquipment.collidepoint(mousePos):
                            equipment=self.inventory.currentDrawlist[i]
                            if equipment.slot=='sword':
                                if self.inventory.existSlotForEquipment(equipment):
                                    self.inventory.equipEquipment(equipment)
                                else:
                                    self.inventory.switchEquipment(equipment,'sword')
                            elif equipment.slot=='shield':
                                if self.inventory.existSlotForEquipment(equipment):
                                    self.inventory.equipEquipment(equipment)
                                else:
                                    self.inventory.switchEquipment(equipment,'shield')
                            elif equipment.slot=='accessory':
                                if self.inventory.existSlotForEquipment(equipment):
                                    self.inventory.equipEquipment(equipment)
                                else:
                                    self.selectingAccessory=True
                                    self.selectedEquipment=equipment

    def selectionSwitchAccessory(self,events):
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rectSlotAccessory1.collidepoint(mousePos):
                        self.inventory.switchEquipment(self.selectedEquipment,'accessory1')
                    elif self.rectSlotAccessory2.collidepoint(mousePos):
                        self.inventory.switchEquipment(self.selectedEquipment,'accessory2')
                    elif self.rectSlotAccessory3.collidepoint(mousePos):
                        self.inventory.switchEquipment(self.selectedEquipment,'accessory3')
                    self.selectingAccessory=False
                                    


                        





    def handle_events(self, events):
        if self.selectingAccessory:
            self.selectionSwitchAccessory(events)
        else:
            self.scrollInventory(events)
            self.updateButtonsEvents(events)
            self.buttonEquipment(events)

