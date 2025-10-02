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
        self.speed = 200  # pixels par seconde
        self.jump_force = 500  # force de saut
        self.on_ground = False
        self.coyote_time_max = 0.15  # 150ms en secondes
        self.coyote_timer = 0

        # Créer le corps physique
        mass = 1
        moment = pymunk.moment_for_box(mass, (self.rect.width, self.rect.height))
        self.body = pymunk.Body(mass, moment, pymunk.Body.DYNAMIC)
        self.body.position = pos

        # Créer la forme de collision
        self.shape = pymunk.Poly.create_box(self.body, (self.rect.width, self.rect.height))
        self.shape.friction = 0.7
        self.shape.collision_type = 1

        # Ajouter à l'espace physique
        self.space.add(self.body, self.shape)

    def check_ground(self):
        """Vérification du sol avec un seul point"""
        point_to_check = (
            self.body.position.x,
            self.body.position.y + self.rect.height // 2 + 3
        )

        query = self.space.point_query_nearest(point_to_check, 5, pymunk.ShapeFilter())
        if query and query.shape and query.shape != self.shape:
            # Si on monte trop vite, on n'est pas vraiment au sol
            if self.body.velocity.y > -100:
                return True

        return False

    def input(self, dt):
        keys = pygame.key.get_pressed()

        # Vérifier si on est au sol
        self.on_ground = self.check_ground()

        # Gestion du coyote timer
        if self.on_ground:
            self.coyote_timer = self.coyote_time_max
        elif self.coyote_timer > 0:
            self.coyote_timer -= dt

        # Mouvement horizontal - applique une force
        target_velocity_x = 0
        if keys[pygame.K_d]:
            target_velocity_x = self.speed
        elif keys[pygame.K_q]:
            target_velocity_x = -self.speed

        # Calculer la force nécessaire
        velocity_diff = target_velocity_x - self.body.velocity.x
        force_x = velocity_diff * self.body.mass * 15

        # Appliquer la force horizontale
        self.body.apply_force_at_local_point((force_x, 0), (0, 0))

        # Limiter la vitesse horizontale maximale
        if abs(self.body.velocity.x) > self.speed:
            self.body.velocity = (
                self.speed * (1 if self.body.velocity.x > 0 else -1),
                self.body.velocity.y
            )

        # Saut avec coyote time
        if keys[pygame.K_SPACE] and self.coyote_timer > 0:
            # Appliquer l'impulsion de saut
            impulse_y = -self.jump_force * self.body.mass
            self.body.apply_impulse_at_local_point((0, impulse_y), (0, 0))
            self.coyote_timer = 0  # Réinitialiser pour éviter le double saut

    def update(self, dt):
        self.input(dt)

        # Empêcher la rotation
        self.body.angle = 0
        self.body.angular_velocity = 0

        # Friction dans l'air pour un meilleur contrôle
        if not self.on_ground:
            self.body.velocity = (
                self.body.velocity.x * 0.98,
                self.body.velocity.y
            )

        # Synchroniser la position du sprite avec le corps physique
        self.rect.center = (int(self.body.position.x), int(self.body.position.y))

    def setSpawnPoint(self, spawnPoint):
        self.body.position = spawnPoint
        self.body.velocity = (0, 0)
        self.rect.center = spawnPoint