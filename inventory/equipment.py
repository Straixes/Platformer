import pygame
import os
class equipment():
    def __init__(self,name,slot,level,experience,quality,effect,damageBoost,armourBoost,healthBoost):
        self.name=name
        spritPath = os.path.join(os.path.dirname(__file__), "equipmentImage",slot, name+".png")
        sprit=pygame.image.load(spritPath).convert_alpha()
        self.sprit=pygame.transform.scale(sprit, (160,160))
        self.slot=slot
        self.level=level
        self.experience=experience
        self.experienceNeedToUpgrade=(self.level**2)*10

        self.quality = quality #Rusted / Forged / Enchanted / Blessed / Divine
        self.qualitySortDict={"rusted":1,"forged":2,"enchanted":3,"blessed":4,"divine":5} 
        self.qualitySort=self.qualitySortDict[quality]
        self.qualityUpgradeStatBoostDict={"rusted":1.01,"forged":1.02,"enchanted":1.035,"blessed":1.045,"divine":1.06}
        self.qualityUpgradeStatBoost=self.qualityUpgradeStatBoostDict[quality]
        qualitySpritPath = os.path.join(os.path.dirname(__file__), "equipmentImage","quality", quality+".png")
        qualitySprit=pygame.image.load(qualitySpritPath).convert_alpha()
        self.qualitySprit=pygame.transform.scale(qualitySprit, (160,160))

        self.effect=effect
        self.damageBoost=damageBoost
        self.armourBoost=armourBoost
        self.healthBoost=healthBoost
    
    def getExperienceNeedToLevelUp(self):
        return (self.level**2)*10

    def addExperience(self,amount):
        if self.experience+amount<self.experienceNeedToUpgrade:
            self.experience+=amount
        else:
            self.level+=1
            self.experience=self.experience+amount-self.experienceNeedToUpgrade
            self.experienceNeedToUpgrade=self.getExperienceNeedToLevelUp()

    def upgrade(self):
        if self.damageBoost!=0:
            self.damageBoost=self.damageBoost*self.qualityUpgradeStatBoost+1
        if self.armourBoost!=0:
            self.armourBoost=self.armourBoost*self.qualityUpgradeStatBoost+1
        if self.healthBoost!=0:
            self.healthBoost=self.healthBoost*self.qualityUpgradeStatBoost+1

    def draw(self,screen,slotPosX,slotPosY):
        screen.blit(self.qualitySprit,(slotPosX,slotPosY))
        screen.blit(self.sprit,(slotPosX,slotPosY))
        ratio = min(1,self.experience/self.experienceNeedToUpgrade)
        pygame.draw.rect(screen, (0, 204, 203), (slotPosX,slotPosY+150,int(ratio*160),10))
