import settings
from entities.Obstacle import Obstacle
import pygame

class Plateform(Obstacle):
    def __init__(self, sprite_name, x, y, velocity, game ,isMoving=False, distanceMoving=0):
        super().__init__(sprite_name, x, y)
        self.velocity = velocity
        self.isMoving = isMoving
        self.distanceMoving = distanceMoving

        # Variables de mouvement
        self.start_x = x               # position de départ
        self.direction = 1             # 1 = droite, -1 = gauche
        self.distance_traveled = 0     # distance parcourue depuis le dernier demi-tour
        self.game = game

    def update(self):
        if self.isMoving:
            # Déplace la plateforme
            self.rect.x += self.velocity * self.direction
            self.distance_traveled += abs(self.velocity)

            if self.rect.x >= settings.SCREEN_WIDTH - self.width or self.rect.x <= self.width:
                self.direction *= -1
                self.distance_traveled = 0

            # Vérifie les collisions
            obsHits = [o for o in
                       pygame.sprite.spritecollide(self, self.game.allDiffObstacles, False, pygame.sprite.collide_mask)
                       if o != self]
            if obsHits:
                # Demi-tour après collision
                self.direction *= -1
                self.distance_traveled = 0

            # Demi-tour si la distance max est atteinte
            if self.distance_traveled >= self.distanceMoving:
                self.direction *= -1
                self.distance_traveled = 0