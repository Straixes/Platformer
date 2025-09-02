from entities.Obstacle import Obstacle

class Plateform(Obstacle):
    def __init__(self, width, height, sprite_name, x, y, velocity, isMoving=False, distanceMoving=0):
        super().__init__(width, height, sprite_name, x, y)
        self.velocity = velocity
        self.isMoving = isMoving
        self.distanceMoving = distanceMoving

        # Variables de mouvement
        self.start_x = x               # position de départ
        self.direction = 1             # 1 = droite, -1 = gauche
        self.distance_traveled = 0     # distance parcourue depuis le dernier demi-tour

    def update(self):
        if self.isMoving:
            # Avance dans la direction actuelle
            self.rect.x += self.velocity * self.direction
            self.distance_traveled += self.velocity

            # Si la distance max est atteinte → demi-tour
            if self.distance_traveled >= self.distanceMoving:
                self.direction *= -1
                self.distance_traveled = 0
