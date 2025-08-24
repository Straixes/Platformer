import pygame
from entities.Player import Player
from entities.Obstacle import Obstacle
from utils.physics import move_player
import settings

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

        # Groupes
        self.obstacles = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()

        # Joueur
        self.player = Player("Quentin", 100, "sprite", settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT, 200, settings.GROUND_Y - settings.PLAYER_HEIGHT, 1, screen)
        self.player_group.add(self.player)

        # Obstacles
        self.create_obstacles()

        # Font FPS
        self.font = pygame.font.SysFont("Arial", 24)

    def create_obstacles(self):
        obs1 = Obstacle(64, 64, "obstacleTest", 360, settings.GROUND_Y - 64)
        obs2 = Obstacle(64, 64, "obstacleTest", 500, settings.GROUND_Y - 128)
        obs3 = Obstacle(64, 64, "obstacleTest", 800, settings.GROUND_Y - 148)
        self.obstacles.add(obs1, obs2, obs3)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt, keys):
        move_player(self.player, keys, dt, settings.PLAYER_SPEED, settings.GRAVITY, settings.JUMP_FORCE, settings.GROUND_Y, self.obstacles)
        self.player.update_state(keys)

    def draw(self):
        self.screen.fill("gray")

        # Sol
        pygame.draw.line(self.screen, "white", (0, settings.GROUND_Y), (settings.SCREEN_WIDTH, settings.GROUND_Y), 5)

        # Joueur
        self.player.draw()
        self.player.draw_health_bar()

        # Obstacles
        for obs in self.obstacles:
            obs.draw(self.screen)

        # FPS
        fps_text = self.font.render(f"FPS: {int(self.clock.get_fps())}", True, pygame.Color("white"))
        self.screen.blit(fps_text, (10, 10))

        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(settings.FPS) / 1000
            keys = pygame.key.get_pressed()
            self.handle_events()
            self.update(dt, keys)
            self.draw()
