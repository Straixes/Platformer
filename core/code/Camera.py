import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.displaySurface = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2()
        self.halfW = self.displaySurface.get_size()[0] // 2
        self.halfH = self.displaySurface.get_size()[1] // 2

        # box setup
        self.cameraBorders = {'left': 550, 'right': 550, 'top': 125, 'bottom': 125}
        l = self.cameraBorders['left']
        t = self.cameraBorders['top']
        w = self.displaySurface.get_size()[0] - (self.cameraBorders['left'] + self.cameraBorders['right'])
        h = self.displaySurface.get_size()[1] - (self.cameraBorders['top'] + self.cameraBorders['bottom'])
        self.cameraRect = pygame.Rect(l, t, w, h)

    def centerTargetCamera(self, target):
        self.offset.x = target.rect.centerx - self.halfW
        self.offset.y = target.rect.centery - self.halfH

    def boxTargetCamera(self, target):

        if target.rect.left < self.cameraRect.left:
            self.cameraRect.left = target.rect.left
        if target.rect.right > self.cameraRect.right:
            self.cameraRect.right = target.rect.right
        if target.rect.top < self.cameraRect.top:
            self.cameraRect.top = target.rect.top
        if target.rect.bottom > self.cameraRect.bottom:
            self.cameraRect.bottom = target.rect.bottom

        self.offset.x = self.cameraRect.left - self.cameraBorders['left']
        self.offset.y = self.cameraRect.top - self.cameraBorders['top']

    def customDraw(self, player):

        #self.centerTargetCamera(player)
        self.boxTargetCamera(player)

        # active elements
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.image, offsetPos)

        #pygame.draw.rect(self.displaySurface, 'yellow' , self.cameraRect, 5)