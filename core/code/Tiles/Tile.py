import pygame
import pymunk


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, space):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

        #Pour le moment pas utile mais possibilité de l'utiliser plus tard
        #self.tileMask = pygame.mask.from_surface(self.image)

        # Créer un corps statique pour les tiles
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)

        # IMPORTANT: Position du centre du corps (Pymunk utilise le centre)
        center_x = pos[0] + self.rect.width // 2
        center_y = pos[1] + self.rect.height // 2
        self.body.position = (center_x, center_y)

        # Créer la forme avec les bonnes dimensions
        self.shape = pymunk.Poly.create_box(self.body, (self.rect.width, self.rect.height))

        # CRUCIAL: Propriétés de collision
        self.shape.friction = 0.7

        # Ajouter le corps et la forme à l'espace physique
        space.add(self.body, self.shape)


