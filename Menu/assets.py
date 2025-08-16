import pygame
import time
class buttonText:
    def __init__(self,posX,posY,sizeX,sizeY,fonction,text,colorText,color,colorPressed,font):
        self.buttonRect=pygame.Rect(posX, posY, sizeX, sizeY)

        self.posX=posX
        self.posY=posY
        self.sizeX=sizeX
        self.sizeY=sizeY

        self.color=color
        self.fonction=fonction
        self.text=text
        self.colorPressed=colorPressed
        self.font=font
        self.colorText=colorText

        self.lastTimePressed=0
        self.cooldown=0.35
    
    #Changement de taille
    def sizeUpdate(self,resolution):
        coefX,coefY=resolution[0]/1920,resolution[1]/1080
        self.buttonRect=pygame.Rect(self.posX*coefX, self.posY*coefY, self.sizeX*coefX, self.sizeY*coefY)
    #detecte si curseur sur bouton
    def isOnButton(self,mousePos):
        return self.buttonRect.collidepoint(mousePos)

    def draw(self,mousePos,screen):
        if self.isOnButton(mousePos):
            pygame.draw.rect(screen, self.colorPressed, self.buttonRect)
        else:
            pygame.draw.rect(screen, self.color, self.buttonRect)

        text_surface = self.font.render(self.text, True, self.colorText)
        text_rect = text_surface.get_rect(center=self.buttonRect.center)
        screen.blit(text_surface, text_rect)

    def update(self,resolution,mousePos,mouseClick,screen,changeResolution):

        if changeResolution:
            self.sizeUpdate(resolution)

        self.draw(mousePos,screen)
        if mouseClick[0] and self.isOnButton(mousePos):
            actualTime=time.time()
            if actualTime - self.lastTimePressed >= self.cooldown:
                self.lastTimePressed=actualTime
                self.fonction()

class buttonImage:
    def __init__(self,posX,posY,sizeX,sizeY,fonction,image,imagePressed):
        self.buttonRect=pygame.Rect(posX, posY, sizeX, sizeY)

        self.posX=posX
        self.posY=posY
        self.sizeX=sizeX
        self.sizeY=sizeY

        self.fonction=fonction
        self.image=pygame.transform.scale(image, (self.buttonRect.width, self.buttonRect.height))
        self.imagePressed=pygame.transform.scale(imagePressed, (self.buttonRect.width, self.buttonRect.height))

        self.lastTimePressed=0
        self.cooldown=0.35

        
    
    #Changement de taille
    
    def sizeUpdate(self,resolution):
        coefX,coefY=resolution[0]/1920,resolution[1]/1080
        self.buttonRect=pygame.Rect(self.posX*coefX, self.posY*coefY, self.sizeX*coefX, self.sizeY*coefY)
        self.image=pygame.transform.scale(self.image, (self.buttonRect.width, self.buttonRect.height))
        self.imagePressed=pygame.transform.scale(self.imagePressed, (self.buttonRect.width, self.buttonRect.height))

    #detecte si curseur sur bouton
    def isOnButton(self,mousePos):
        return self.buttonRect.collidepoint(mousePos)

    def draw(self,mousePos,screen):
        if self.isOnButton(mousePos):
            screen.blit(self.imagePressed, self.buttonRect.topleft)
        else:
            screen.blit(self.image, self.buttonRect.topleft)

        

    def update(self,resolution,mousePos,mouseClick,screen,changeResolution):
        if changeResolution:
            self.sizeUpdate(resolution)

        self.draw(mousePos,screen)

        if mouseClick[0] and self.isOnButton(mousePos):
            actualTime=time.time()
            if actualTime - self.lastTimePressed >= self.cooldown:
                self.lastTimePressed=actualTime
                self.fonction()
                


class text():
    def __init__(self,text,size,color,center,font=None): 
        self.text=text
        self.font=font
        self.size=size
        self.color=color
        self.center=center
    
    def blitText(self,screen):
        font = pygame.font.Font(self.font, self.size)
        text_surface = font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=self.center)
        screen.blit(text_surface, text_rect)

class textsSettings():
    def __init__(self,texts,size,color,center,font=None): 
        self.texts=texts
        self.currentTextIndex=len(texts)-1 #a changer plus tard il faut sauvegarder les parametres
        self.font=font
        self.size=size
        self.color=color
        self.center=center
    
    def getCurrentText(self):
        return self.texts[self.currentTextIndex]
    
    def blitText(self,screen):
        font = pygame.font.Font(self.font, self.size)
        text_surface = font.render(self.getCurrentText(), True, self.color)
        text_rect = text_surface.get_rect(center=self.center)
        screen.blit(text_surface, text_rect)

    def nextText(self):
        self.currentTextIndex=(self.currentTextIndex+1) % len(self.texts)
    
    def previousText(self):
        self.currentTextIndex=(self.currentTextIndex-1) % len(self.texts)

    
