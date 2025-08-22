
class inventory():
    def __init__(self):
        self.equipmentList=[]
        self.currentSortlist=[]
        self.currentDrawlist=[]
        self.drawListLine=None
        self.slotSword=None
        self.slotShield=None
        self.slotAccessory1=None
        self.slotAccessory2=None
        self.slotAccessory3=None
    
    def addEquipment(self,equipment):
        self.equipmentList.append(equipment)

    def removeEquipment(self,equipmentRemove):
        self.equipmentList.remove(equipmentRemove)
    
    def sortEquipment(self,slot,functionSortElement,decroissant):
        listSlot=[equipment for equipment in self.equipmentList if equipment.slot == slot]
        self.currentSortlist = sorted(listSlot, key= functionSortElement, reverse=decroissant)
        self.drawListLine=0
        self.updateDrawList()
    
    def increaseLign(self):
        if len(self.currentSortlist)>(self.drawListLine*5+25):
            self.drawListLine+=1
            self.updateDrawList()
            
    
    def decreaseLign(self):
        if self.drawListLine>0:
            self.drawListLine-=1
            self.updateDrawList()

    def fonctionDrawEquipment(self,screen):
        def drawEquipments():

            lenList=len(self.currentDrawlist)
            for i in range(lenList):
                self.currentDrawlist[i].draw(screen,965+175*(i%5),165+175*(i//5))
        return drawEquipments

    def updateDrawList(self):
        self.currentDrawlist=self.currentSortlist[self.drawListLine*5:min((self.drawListLine+5)*5,len(self.currentSortlist))]

    def isSlotSwordEmpty(self):
        return self.slotSword==None
    
    def isSlotShieldEmpty(self):
        return self.slotShield==None
    
    def isSlotAccessory1Empty(self):
        return self.slotAccessory1==None
    
    def isSlotAccessory2Empty(self):
        return self.slotAccessory2==None
    
    def isSlotAccessory3Empty(self):
        return self.slotAccessory3==None
    
    def isOneAccessorySlotEmpty(self):
        return self.slotAccessory1 or self.slotAccessory2 or self.slotAccessory3
    
    def existSlotForEquipment(self,equipment):
        dictSlot={'sword' : self.isSlotSwordEmpty,
                  'shield': self.isSlotShieldEmpty,
                  'accessoty': self.isOneAccessorySlotEmpty}
        return dictSlot[equipment.slot]()
    
    
    