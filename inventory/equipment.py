class equipment():
    def __init__(self,name,sprit,slot,level,experience,quality,effect,damageBoost,armourBoost,healthBoost):
        self.name=name
        self.sprit=sprit
        self.slot=slot
        self.level=level
        self.experience=experience

        self.quality = quality #Rusted / Forged / Enchanted / Blessed / Divine
        self.qualitySortDict={"Rusted":1,"Forged":2,"Enchanted":3,"Blessed":4,"Divine":5} 
        self.qualitySort=self.qualitySortDict[quality]
        self.qualityUpgradeStatBoostDict={"Rusted":1.01,"Forged":1.02,"Enchanted":1.035,"Blessed":1.045,"Divine":1.06}
        self.qualityUpgradeStatBoost=self.qualityUpgradeStatBoostDict[quality]

        self.effect=effect
        self.damageBoost=damageBoost
        self.armourBoost=armourBoost
        self.healthBoost=healthBoost
    
    def getExperienceNeedToLevelUp(self):
        return (self.level**2)*10

    def addExperience(self,amount):
        expNeed=self.getExperienceNeedToLevelUp()
        if self.experience+amount<expNeed:
            self.experience+=amount
        else:
            self.level+=1
            self.experience=self.experience+amount-expNeed

    def upgradeEquipment(self):
        if self.damageBoost!=0:
            self.damageBoost=self.damageBoost*self.qualityUpgradeStatBoost+1
        if self.armourBoost!=0:
            self.armourBoost=self.armourBoost*self.qualityUpgradeStatBoost+1
        if self.healthBoost!=0:
            self.healthBoost=self.healthBoost*self.qualityUpgradeStatBoost+1
