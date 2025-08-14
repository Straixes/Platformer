import pygame
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
            self.fonction()