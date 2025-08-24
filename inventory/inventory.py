
class inventory():
    def __init__(self):
        self.equipmentList=[]
        self.currentSortlist=[]
        self.currentDrawlist=[]
        self.drawListLine=0
        self.dictSlot={
            "sword": None,
            "shield": None,
            "accessory1": None,
            "accessory2": None,
            "accessory3": None
        }

        self.lastSortSlot='sword'
        self.lastSortFunction= lambda x : x.level
        self.lastSortOrder=False

    
    def addEquipment(self,equipment):
        self.equipmentList.append(equipment)
        self.updateDrawList()

    def removeEquipment(self,equipmentRemove):
        self.equipmentList.remove(equipmentRemove)
        self.updateDrawList()
    
    def sortEquipment(self,slot,functionSortElement,decroissant):
        listSlot=[equipment for equipment in self.equipmentList if equipment.slot == slot]
        self.currentSortlist = sorted(listSlot, key= functionSortElement, reverse=decroissant)
        self.drawListLine=0
        self.lastSortSlot=slot
        self.lastSortFunction= functionSortElement
        self.lastSortOrder=decroissant
        self.updateDrawList()
    
    def increaseLign(self):
        if len(self.currentSortlist)>(self.drawListLine*5+25):
            self.drawListLine+=1
            self.updateDrawList()
            
    
    def decreaseLign(self):
        if self.drawListLine>0:
            self.drawListLine-=1
            self.updateDrawList()



    def updateDrawList(self):
        listSlot=[equipment for equipment in self.equipmentList if equipment.slot == self.lastSortSlot]
        self.currentSortlist = sorted(listSlot, key= self.lastSortFunction, reverse=self.lastSortOrder)
        self.currentDrawlist=self.currentSortlist[self.drawListLine*5:min((self.drawListLine+5)*5,len(self.currentSortlist))]

    def isSlotSwordEmpty(self):
        return self.dictSlot['sword']==None
    
    def isSlotShieldEmpty(self):
        return self.dictSlot['shield']==None
    
    def isSlotAccessory1Empty(self):
        return self.dictSlot['accessory1']==None
    
    def isSlotAccessory2Empty(self):
        return self.dictSlot['accessory2']==None
    
    def isSlotAccessory3Empty(self):
        return self.dictSlot['accessory3']==None
    
    def isOneAccessorySlotEmpty(self):
        return self.isSlotAccessory1Empty() or self.isSlotAccessory2Empty() or self.isSlotAccessory3Empty()
    
    def existSlotForEquipment(self,equipment):
        dictSlot={'sword' : self.isSlotSwordEmpty,
                  'shield': self.isSlotShieldEmpty,
                  'accessory': self.isOneAccessorySlotEmpty}
        return dictSlot[equipment.slot]()
    
    def equipEquipment(self,equipment):
        if self.existSlotForEquipment(equipment):
            if equipment.slot=='sword':
                self.dictSlot['sword']=equipment
            if equipment.slot=='shield':
                self.dictSlot['shield']=equipment
            if equipment.slot=='accessory':
                if self.isSlotAccessory1Empty():
                    self.dictSlot['accessory1']=equipment
                elif self.isSlotAccessory2Empty():
                    self.dictSlot['accessory2']=equipment
                elif self.isSlotAccessory3Empty():
                    self.dictSlot['accessory3']=equipment
            self.removeEquipment(equipment)

    def switchEquipment(self,equipment,slot):
        if self.dictSlot[slot]!=None:
            self.addEquipment(self.dictSlot[slot])
            self.dictSlot[slot]=equipment
            self.removeEquipment(equipment)

    def unequipEquipment(self,slot):
        if self.dictSlot[slot]!=None:
            self.addEquipment(self.dictSlot[slot])
            self.dictSlot[slot]=None
            



    
    
    