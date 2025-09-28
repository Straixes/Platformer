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
        self.speed = 200          # pixels par seconde
        self.jump_force = 500     # force de saut
        self.on_ground = False
        self.coyote_time = 0
        self.coyote_time_max = 6  # frames

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

    def input(self, dt):
        keys = pygame.key.get_pressed()
        self.check_ground()

        # Mouvement horizontal
        target_velocity_x = 0
        if keys[pygame.K_d]:
            target_velocity_x = self.speed
        elif keys[pygame.K_q]:
            target_velocity_x = -self.speed

        # Interpolation douce
        current_velocity_x = self.body.velocity.x
        velocity_diff = target_velocity_x - current_velocity_x
        acceleration = 0.3 if self.on_ground else 0.15
        new_velocity_x = current_velocity_x + velocity_diff * acceleration

        # Appliquer la vitesse horizontale (indépendante du FPS)
        self.body.velocity = (new_velocity_x, self.body.velocity.y)

        # Saut avec coyote time
        if keys[pygame.K_SPACE] and (self.on_ground or self.coyote_time > 0):
            self.body.velocity = (self.body.velocity.x, -self.jump_force)
            self.coyote_time = 0

    def update(self, dt):
        self.input(dt)

        # Empêcher la rotation
        self.body.angular_velocity = 0

        # Synchroniser la position du sprite avec le corps physique
        self.rect.center = (int(self.body.position.x), int(self.body.position.y))

    def setSpawnPoint(self, spawnPoint):
        self.body.position = spawnPoint
        self.rect.center = spawnPoint
