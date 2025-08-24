import pygame
import os
from entities.Personnage import Personnage

class Player(Personnage):
    def __init__(self, name, health, sprite_name, width, height, x, y, level, screen):
        super().__init__(name, health, width, height, x, y, level)
        self.screen = screen
        self.sprite_name = sprite_name

        self.sprites = {
            "idle": pygame.image.load(os.path.join("img", f"{sprite_name}.png")).convert_alpha(),
            "forward": pygame.image.load(os.path.join("img", f"{sprite_name}Forward.png")).convert_alpha(),
            "backward": pygame.image.load(os.path.join("img", f"{sprite_name}Backward.png")).convert_alpha(),
            "jump": pygame.image.load(os.path.join("img", f"{sprite_name}RightJump.png")).convert_alpha()
        }

        self.state = "idle"
        self.texture = self.sprites[self.state]
        self.mask = pygame.mask.from_surface(self.texture)
        self.velocity_y = 0

    def update_state(self, keys):
        if self.velocity_y < 0:
            self.state = "jump"
        elif keys[pygame.K_q]:
            self.state = "backward"
        elif keys[pygame.K_d]:
            self.state = "forward"
        else:
            self.state = "idle"

        self.texture = self.sprites[self.state]
        self.mask = pygame.mask.from_surface(self.texture)

    def draw(self):
        self.screen.blit(self.texture, self.rect.topleft)

    def draw_health_bar(self):
        pygame.draw.rect(self.screen, (200, 0, 0), (10, 10, 200, 20))
        pygame.draw.rect(self.screen, (0, 200, 0), (10, 10, (self.health / 100) * 200, 20))
