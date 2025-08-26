import pygame
import time
import os
class buttonText:
    def __init__(self,posX,posY,sizeX,sizeY,fonction,text,colorText,color,colorPressed,font,canHold=False):
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

        self.canHold=canHold
        self.lastTimePressed=0
        self.cooldown=0.15
    
    #Changement de taille
    def updateSize(self,resolution):
        coefX,coefY=resolution[0]/1920,resolution[1]/1080
        self.buttonRect=pygame.Rect(self.posX*coefX, self.posY*coefY, self.sizeX*coefX, self.sizeY*coefY)
    #detecte si curseur sur bouton
    def isOnButton(self,mousePos):
        return self.buttonRect.collidepoint(mousePos)

    def draw(self,screen,mousePos):
        if self.isOnButton(mousePos):
            pygame.draw.rect(screen, self.colorPressed, self.buttonRect)
        else:
            pygame.draw.rect(screen, self.color, self.buttonRect)

        text_surface = self.font.render(self.text, True, self.colorText)
        text_rect = text_surface.get_rect(center=self.buttonRect.center)
        screen.blit(text_surface, text_rect)

    def update(self,mouseClick,mouseGetClicked,mousePos):
        if mouseGetClicked and self.buttonRect.collidepoint(mousePos):
            self.lastTimePressed=time.time()
            self.fonction()   
        elif mouseClick[0]==1 and self.canHold:
            actualTime=time.time()
            if self.buttonRect.collidepoint(mousePos) and actualTime - self.lastTimePressed >= self.cooldown:
                self.lastTimePressed=actualTime
                self.fonction()

class buttonImage:
    def __init__(self,posX,posY,sizeX,sizeY,fonction,imageName,imagePressedName,canHold=False):
        self.buttonRect=pygame.Rect(posX, posY, sizeX, sizeY)

        self.posX=posX
        self.posY=posY
        self.sizeX=sizeX
        self.sizeY=sizeY

        self.fonction=fonction
        self.imageName=imageName
        imagePath = os.path.join(os.path.dirname(__file__), "textureButton", imageName)
        image=pygame.image.load(imagePath).convert_alpha()
        self.image=pygame.transform.scale(image, (self.buttonRect.width, self.buttonRect.height))
        self.initialImage=self.image
        self.mask = pygame.mask.from_surface(self.initialImage)

        self.imagePressedName=imagePressedName
        imagePressedPath = os.path.join(os.path.dirname(__file__), "textureButton", imagePressedName)
        imagePressed=pygame.image.load(imagePressedPath).convert_alpha()
        self.imagePressed=pygame.transform.scale(imagePressed, (self.buttonRect.width, self.buttonRect.height))
        self.initialImagePressed=self.imagePressed

        self.canHold=canHold
        self.lastTimePressed=0
        self.cooldown=0.15

        
    
    #Changement de taille
    
    def updateSize(self,resolution):
        coefX,coefY=resolution[0]/1920,resolution[1]/1080
        self.buttonRect=pygame.Rect(self.posX*coefX, self.posY*coefY, self.sizeX*coefX, self.sizeY*coefY)
        self.image=pygame.transform.scale(self.initialImage, (self.buttonRect.width, self.buttonRect.height))
        self.imagePressed=pygame.transform.scale(self.initialImagePressed, (self.buttonRect.width, self.buttonRect.height))
        self.mask = pygame.mask.from_surface(self.image)

    #detecte si curseur sur bouton
    def isOnButton(self,mousePos):
        if self.buttonRect.collidepoint(mousePos):
            offset = (mousePos[0] - self.buttonRect.x, mousePos[1] - self.buttonRect.y)
            return self.mask.get_at(offset)
        return False

    def draw(self,screen,mousePos):
        if self.isOnButton(mousePos):
            screen.blit(self.imagePressed, self.buttonRect.topleft)
        else:
            screen.blit(self.image, self.buttonRect.topleft)

    def update(self,mouseClick,mouseGetClicked,mousePos):
        if mouseGetClicked and self.isOnButton(mousePos):
            self.lastTimePressed=time.time()
            self.fonction()   
        elif mouseClick[0]==1 and self.canHold and self.isOnButton(mousePos):
            actualTime=time.time()
            if actualTime - self.lastTimePressed >= self.cooldown:
                self.lastTimePressed=actualTime
                self.fonction()
    def setImage(self,imageName,imagePressedName):
        self.imageName=imageName
        imagePath = os.path.join(os.path.dirname(__file__), "textureButton", imageName)
        image=pygame.image.load(imagePath).convert_alpha()
        self.image=pygame.transform.scale(image, (self.buttonRect.width, self.buttonRect.height))
        self.initialImage=self.image
        self.mask = pygame.mask.from_surface(self.initialImage)
        self.imagePressedName=imagePressedName
        imagePressedPath = os.path.join(os.path.dirname(__file__), "textureButton", imagePressedName)
        imagePressed=pygame.image.load(imagePressedPath).convert_alpha()
        self.imagePressed=pygame.transform.scale(imagePressed, (self.buttonRect.width, self.buttonRect.height))
        self.initialImagePressed=self.imagePressed

                


class text():
    def __init__(self,text,size,color,center,font=None): 
        self.text=text
        self.font=font
        self.size=size
        self.initialSize=size
        self.color=color
        self.center=center
        self.initialCenter=center
    
    def blitText(self,screen):
        font = pygame.font.Font(self.font, self.size)
        text_surface = font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=self.center)
        screen.blit(text_surface, text_rect)

    def updateSize(self,resolution):
        x,y=self.initialCenter
        coef=resolution[0]/1920
        self.center=(x*coef,y*coef)
        self.size=int(coef*self.initialSize)


class MultiTexts():
    def __init__(self,texts,size,color,center,font=None): 
        self.texts=texts
        self.currentTextIndex=0 
        self.font=font
        self.size=size
        self.initialSize=size
        self.color=color
        self.center=center
        self.initialCenter=center
    
    def getCurrentText(self):
        return self.texts[self.currentTextIndex]
    
    def updateSize(self,resolution):
        x,y=self.initialCenter
        coef=resolution[0]/1920
        self.center=(x*coef,y*coef)
        self.size=int(coef*self.initialSize)

    def setTextTo(self,index):
        self.currentTextIndex=index

    def blitText(self,screen):
        font = pygame.font.Font(self.font, self.size)
        text_surface = font.render(self.getCurrentText(), True, self.color)
        text_rect = text_surface.get_rect(center=self.center)
        screen.blit(text_surface, text_rect)

    def nextText(self):
        self.currentTextIndex=(self.currentTextIndex+1) % len(self.texts)
    
    def previousText(self):
        self.currentTextIndex=(self.currentTextIndex-1) % len(self.texts)

class background():
    def __init__(self,backgroundName):
        backgroundPath = os.path.join(os.path.dirname(__file__), "textureBackground", backgroundName)
        background=pygame.image.load(backgroundPath).convert_alpha()
        self.background=pygame.transform.scale(background, (1920,1080))
        self.initialbackground=self.background

    def blitBackground(self,screen):
        screen.blit(self.background, (0, 0))

    def updateSize(self,resolution):
        self.background=pygame.transform.scale(self.initialbackground, resolution)

class image():
    def __init__(self,posX,posY,sizeX,sizeY,imageName,condition=None):
        self.buttonRect=pygame.Rect(posX, posY, sizeX, sizeY)

        self.posX=posX
        self.posY=posY
        self.sizeX=sizeX
        self.sizeY=sizeY
        self.condition=condition

        
        imagePath = os.path.join(os.path.dirname(__file__), "textureImage", imageName)
        image=pygame.image.load(imagePath).convert_alpha()
        self.image=pygame.transform.scale(image, (self.buttonRect.width, self.buttonRect.height))
        self.initialImage=self.image

        
    
    #Changement de taille
    
    def updateSize(self,resolution):
        coefX,coefY=resolution[0]/1920,resolution[1]/1080
        self.buttonRect=pygame.Rect(self.posX*coefX, self.posY*coefY, self.sizeX*coefX, self.sizeY*coefY)
        self.image=pygame.transform.scale(self.initialImage, (self.buttonRect.width, self.buttonRect.height))

    #detecte si curseur sur bouton

    def draw(self,screen):
        if self.condition():
            screen.blit(self.image, self.buttonRect.topleft)
        

    def update(self,screen):
        self.draw(screen)
        
            