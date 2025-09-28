import pygame
import os
import pymunk


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, space):
        super().__init__(group)
        self.base_path = os.path.dirname(__file__)
        self.path = os.path.join(self.base_path, '../../../core/graphics/player/player.png')
        self.image = pygame.image.load(self.path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.space = space

        # Variables de mouvement
        self.speed = 150  # Vitesse horizontale réduite
        self.jump_force = 350
        self.on_ground = False
        self.coyote_time = 0  # Frames où on peut encore sauter après avoir quitté le sol
        self.coyote_time_max = 6

        # Créer le corps physique
        mass = 1
        moment = pymunk.moment_for_box(mass, (self.rect.width, self.rect.height))
        self.body = pymunk.Body(mass, moment, pymunk.Body.DYNAMIC)
        self.body.position = pos

        # Créer la forme de collision
        self.shape = pymunk.Poly.create_box(self.body, (self.rect.width, self.rect.height))
        self.shape.friction = 0.7

        # Ajouter à l'espace physique
        self.space.add(self.body, self.shape)

    def check_ground(self):
        """Vérification du sol améliorée"""
        # Vérifier plusieurs points sous le joueur
        points_to_check = [
            (self.body.position.x - self.rect.width // 4, self.body.position.y + self.rect.height // 2 + 3),
            (self.body.position.x, self.body.position.y + self.rect.height // 2 + 3),
            (self.body.position.x + self.rect.width // 4, self.body.position.y + self.rect.height // 2 + 3)
        ]

        was_on_ground = self.on_ground
        self.on_ground = False

        for point in points_to_check:
            query = self.space.point_query_nearest(point, 0, pymunk.ShapeFilter())
            if query and query.shape and query.shape != self.shape and self.body.velocity.y > -30:
                self.on_ground = True
                break

        # Gestion du coyote time
        if was_on_ground and not self.on_ground:
            self.coyote_time = self.coyote_time_max
        elif self.on_ground:
            self.coyote_time = 0
        elif self.coyote_time > 0:
            self.coyote_time -= 1

    def input(self):
        keys = pygame.key.get_pressed()

        self.check_ground()

        # Mouvement horizontal avec vitesse directe mais limitée
        target_velocity_x = 0

        if keys[pygame.K_d]:
            target_velocity_x = self.speed
        elif keys[pygame.K_q]:
            target_velocity_x = -self.speed

        # Interpolation douce vers la vitesse cible (évite les changements brusques)
        current_velocity_x = self.body.velocity.x
        velocity_diff = target_velocity_x - current_velocity_x

        # Accélération différente selon si on est au sol ou en l'air
        acceleration = 0.3 if self.on_ground else 0.15
        new_velocity_x = current_velocity_x + velocity_diff * acceleration

        # Appliquer la nouvelle vitesse
        self.body.velocity = (new_velocity_x, self.body.velocity.y)

        # Saut avec coyote time
        if keys[pygame.K_SPACE] and (self.on_ground or self.coyote_time > 0):
            self.body.velocity = (self.body.velocity.x, -self.jump_force)
            self.coyote_time = 0

    def update(self):
        self.input()

        # Empêcher la rotation
        self.body.angular_velocity = 0

        # Synchroniser la position
        self.rect.center = (int(self.body.position.x), int(self.body.position.y))

    def setSpawnPoint(self, spawnPoint):
        self.pos = spawnPoint