from state import State 
from .Assets.assets import buttonImage,background,image,text,MultiTexts,getMousePos
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
        self.texts=[text("inventory",50,(122,75,32),(465,80),"UncialAntiqua-Regular.ttf"),
            MultiTexts(['level','quality','damage','health','armour'],30,(122,75,32),(1675,130),"UncialAntiqua-Regular.ttf")]
        self.buttons=[
            buttonImage(960, 30, 75, 125, self.setCurrentEquipmentToSword,"sword.png","swordpressed.png"),
            buttonImage(1040, 30, 75, 125, self.setCurrentEquipmentToShield,"shield.png","shieldpressed.png"),
            buttonImage(1120, 30, 75, 125, self.setCurrentEquipmentToPet,"pet.png","petpressed.png"),
            buttonImage(1200, 30, 75, 125, self.setCurrentEquipmentToAccessory,"accessory.png","accessorypressed.png"),
            buttonImage(1835, 160, 50, 50, self.inventory.decreaseLign,"up.png","upPressed.png"),
            buttonImage(1835, 980, 50, 50,  self.inventory.increaseLign,"down.png","downPressed.png"),
            buttonImage(1575, 105, 200, 50,  self.changeTextSort,"zoneText.png","zoneTextPressed.png")]
        
        self.buttonDecroissant=buttonImage(1780, 105, 50, 50,  self.buttonDecroissantFunction,"decroissant.png","decroissantPressed.png")
        self.buttons.append(self.buttonDecroissant)

        self.images= [
            image(265,305,160,160,"swordIcon.png",self.inventory.isSlotSwordEmpty),
            image(265,530,160,160,"shieldIcon.png",self.inventory.isSlotShieldEmpty),
            image(265,755,160,160,"petIcon.png",self.inventory.isSlotPetEmpty),
            image(510,305,160,160,"accessoryIcon.png",self.inventory.isSlotAccessory1Empty),
            image(510,530,160,160,"accessoryIcon.png",self.inventory.isSlotAccessory2Empty),
            image(510,755,160,160,"accessoryIcon.png",self.inventory.isSlotAccessory3Empty),

            image(960, 30, 75, 125,"swordpressed.png",self.isCurrentEquipmentSword),
            image(1040, 30, 75, 125,"shieldpressed.png",self.isCurrentEquipmentShield),
            image(1120, 30, 75, 125,"petpressed.png",self.isCurrentEquipmentPet),
            image(1200, 30, 75, 125,"accessorypressed.png",self.isCurrentEquipmentAccessory)
        ]
        
        self.dictPosSlot={
            "sword": (265,305),
            "shield": (265,530),
            "pet": (265,305),
            "accessory1": (510,305),
            "accessory2": (510,530),
            "accessory3": (510,755)
        }
        self.scrollRect=pygame.Rect(960,160,870,870)
        self.selectingAccessory=False
        self.selectedEquipment=None

        self.rectSlotSword=pygame.Rect(260,300,170,170)
        self.rectSlotShield=pygame.Rect(260,525,170,170)
        self.rectSlotPet=pygame.Rect(260,750,170,170)
        self.rectSlotAccessory1=pygame.Rect(505,300,170,170)
        self.rectSlotAccessory2=pygame.Rect(505,525,170,170)
        self.rectSlotAccessory3=pygame.Rect(505,750,170,170)

    def changeTextSort(self):
        self.texts[1].nextText()
        funDict={'level' : lambda x : x.level,
                 'quality':lambda x : x.qualitySort,
                 'damage':lambda x : x.damageBoost,
                 'health':lambda x : x.healthBoost,
                 'armour':lambda x : x.armourBoost}
        self.inventory.sortEquipment(self.inventory.lastSortSlot,funDict[self.texts[1].getCurrentText()],self.inventory.lastSortOrder)
    def isCurrentEquipmentSword(self):
        return self.currentEquipment=='sword'
    def isCurrentEquipmentShield(self):
        return self.currentEquipment=='shield'
    def isCurrentEquipmentPet(self):
        return self.currentEquipment=='pet'
    def isCurrentEquipmentAccessory(self):
        return self.currentEquipment=='accessory'
    
    def setCurrentEquipmentToSword(self):
        self.texts[1].setTextTo(0)
        self.inventory.sortEquipment("sword",lambda x : x.level,True)
        self.currentEquipment="sword"
    def setCurrentEquipmentToShield(self):
        self.texts[1].setTextTo(0)
        self.inventory.sortEquipment("shield",lambda x : x.level,True)
        self.currentEquipment="shield"
    def setCurrentEquipmentToPet(self):
        self.texts[1].setTextTo(0)
        self.inventory.sortEquipment("pet",lambda x : x.level,True)
    def setCurrentEquipmentToAccessory(self):
        self.texts[1].setTextTo(0)
        self.inventory.sortEquipment("accessory",lambda x : x.level,True)
        self.currentEquipment="accessory"
    def buttonDecroissantFunction(self):
        self.inventory.sortEquipment(self.inventory.lastSortSlot,self.inventory.lastSortFunction,not(self.inventory.lastSortOrder))
        button=self.buttonDecroissant
        if button.imageName=="decroissant.png":
            button.setImage("croissant.png","croissantPressed.png")
        else:
            button.setImage("decroissant.png","decroissantPressed.png")

    #######DRAW#######
    def drawEquipments(self,screen):
            lenList=len(self.inventory.currentDrawlist)
            for i in range(lenList):
                self.inventory.currentDrawlist[i].draw(screen,965+175*(i%5),165+175*(i//5))

    def drawBackground(self,screen):
        self.background.blitBackground(screen)
    
    def drawButtons(self,screen,ScreenInfo):
        mouse_pos = getMousePos(ScreenInfo)
        for btn in self.buttons:
            btn.draw(screen,mouse_pos)

    def drawEquipedEquipments(self,screen):
        for key in self.inventory.dictSlot.keys():
            equipment=self.inventory.dictSlot[key]
            if equipment !=None:
                x,y=self.dictPosSlot[key]
                equipment.draw(screen,x,y)
    def blitTexts(self,screen):
        for txt in self.texts:
            txt.blitText(screen)
    def draw_blinking_border(self, screen, rect, base_color=(255, 255, 255), thickness=4, speed=0.0025):
        time = pygame.time.get_ticks()
        alpha = (math.sin(time * speed) +2) / 4  # oscillation entre 0 et 1
        color = (int(base_color[0] * alpha), int(base_color[1] * alpha), int(base_color[2] * alpha))
        pygame.draw.rect(screen, color, rect, thickness)

    def blitImage(self,screen):
        for img in self.images:
            img.update(screen)
    
    def draw(self, screen,ScreenInfo):
        self.drawBackground(screen)
        self.drawButtons(screen,ScreenInfo)
        self.blitImage(screen)
        self.drawEquipments(screen)
        self.drawEquipedEquipments(screen)
        self.blitTexts(screen)

        if self.selectingAccessory:
            self.draw_blinking_border(screen, self.rectSlotAccessory1)
            self.draw_blinking_border(screen, self.rectSlotAccessory2)
            self.draw_blinking_border(screen, self.rectSlotAccessory3)

    ### handle events########
    def updateButtonsEvents(self,events,ScreenInfo):
        mousePos = getMousePos(ScreenInfo)
        mouseClick = pygame.mouse.get_pressed()
        mouseGetClicked = False
        
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:  
                mouseGetClicked = True
        for btn in self.buttons:
            btn.update(mouseClick,mouseGetClicked,mousePos)

    def scrollInventory(self,events,ScreenInfo):
        mousePos = getMousePos(ScreenInfo)
        if self.scrollRect.collidepoint(mousePos):

            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.inventory.decreaseLign()
                    elif event.button == 5:
                        self.inventory.increaseLign()
    
    def buttonEquipment(self,events,ScreenInfo):
        mousePos = getMousePos(ScreenInfo)
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
                            elif equipment.slot=='pet':
                                if self.inventory.existSlotForEquipment(equipment):
                                    self.inventory.equipEquipment(equipment)
                                else:
                                    self.inventory.switchEquipment(equipment,'pet')
                            elif equipment.slot=='accessory':
                                if self.inventory.existSlotForEquipment(equipment):
                                    self.inventory.equipEquipment(equipment)
                                else:
                                    self.selectingAccessory=True
                                    self.selectedEquipment=equipment

    def selectionSwitchAccessory(self,events,ScreenInfo):
        mousePos = getMousePos(ScreenInfo)
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
    def unequipEquipment(self,events,ScreenInfo):
        mousePos = getMousePos(ScreenInfo)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rectSlotSword.collidepoint(mousePos):
                        self.inventory.unequipEquipment('sword')
                    elif self.rectSlotShield.collidepoint(mousePos):
                        self.inventory.unequipEquipment('shield')
                    elif self.rectSlotPet.collidepoint(mousePos):
                        self.inventory.unequipEquipment('pet')
                    elif self.rectSlotAccessory1.collidepoint(mousePos):
                        self.inventory.unequipEquipment('accessory1')
                    elif self.rectSlotAccessory2.collidepoint(mousePos):
                        self.inventory.unequipEquipment('accessory2')
                    elif self.rectSlotAccessory3.collidepoint(mousePos):
                        self.inventory.unequipEquipment('accessory3')
                                    


                        





    def handle_events(self, events,ScreenInfo):
        if self.selectingAccessory:
            self.selectionSwitchAccessory(events,ScreenInfo)
        else:
            self.scrollInventory(events,ScreenInfo)
            self.updateButtonsEvents(events,ScreenInfo)
            self.unequipEquipment(events,ScreenInfo)
            self.buttonEquipment(events,ScreenInfo)

