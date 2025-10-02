import pygame
from core.code.Tiles.Tile import Tile

class MouvingTile(Tile):
    def __init__(self, pos, surf, groups, space, isMoving=False, distanceMoving=0, velocity=0):
        super().__init__( pos, surf, groups, space)
        self.velocity = velocity
        self.isMoving = isMoving
        self.distanceMoving = distanceMoving

        self.start_x = pos[0]  # position de départ
        self.direction = 1  # 1 = droite, -1 = gauche
        self.distance_traveled = 0  # distance parcourue depuis le dernier demi-tour

    def update(self, dt):
        self.rect.x += self.velocity * self.direction

        self.distance_traveled += abs(self.velocity)

        if self.rect.x >= 1080 - self.rect.width or self.rect.x <= self.rect.width:
            self.direction *= -1

            self.distance_traveled = 0

        # Vérifie les collisions

        """"
        obsHits = [o for o in
                   pygame.sprite.spritecollide(self, self.game.allDiffObstacles, False, pygame.sprite.collide_mask)
                   if o != self]

        if obsHits:
            # Demi-tour après collision
            self.direction *= -1
            self.distance_traveled = 0
        """