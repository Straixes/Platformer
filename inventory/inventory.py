
class inventory():
    def __init__(self):
        self.equipmentList=[]
    
    def addEquipment(self,equipment):
        self.equipmentList.append(equipment)

    def removeEquipment(self,equipmentRemove):
        self.equipmentList.remove(equipmentRemove)
    
    def sortEquipment(self,slot,functionSortElement,decroissant):
        listSlot=[equipment for equipment in self.equipmentList if equipment.slot == slot]
        return sorted(listSlot, key= functionSortElement, reverse=decroissant)