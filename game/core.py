import pygame
from entities import Player, Obstacle, Plateform
from utils import move_player
import settings


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

        # Groupes
        self.obstacles = pygame.sprite.Group()
        self.plateforms = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()

        self.allDiffObstacles = pygame.sprite.Group()

        # Joueur
        self.player = Player("Quentin", 100, "sprite", settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT, 200, settings.GROUND_Y - settings.PLAYER_HEIGHT, 1, screen)
        self.player_group.add(self.player)

        # Obstacles
        self.create_obstacles()

        #Plateform
        self.createPlateform()

        #Fond
        """
        self.coordBackground = (0, 0)
        self.background = pygame.image.load("img/fond/fond.jpg").convert()
        self.background = pygame.transform.scale(
            self.background,
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        )
"""
        # Font FPS
        self.font = pygame.font.SysFont("Arial", 24)

    def create_obstacles(self):
        obs1 = Obstacle(64, 64, "obstacleTest", 360, settings.GROUND_Y - 64)
        obs2 = Obstacle(64, 64, "obstacleTest", 500, settings.GROUND_Y - 128)
        self.obstacles.add(obs1, obs2)
        self.allDiffObstacles.add(obs1, obs2)


    def createPlateform(self):
        plateform = Plateform(32, 4, "plateform", 700, settings.GROUND_Y - 64, 2, self)
        plateform.isMoving = True
        plateform.distanceMoving = 125
        self.plateforms.add(plateform)
        self.allDiffObstacles.add(plateform)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt, keys):
        move_player(self.player, keys, dt, settings.PLAYER_SPEED, settings.GRAVITY, settings.JUMP_FORCE, settings.GROUND_Y, self.allDiffObstacles)
        self.player.update_state(keys)

        for obs in self.allDiffObstacles:
            if hasattr(obs, "update"):  # seulement si l'objet a une méthode update
                obs.update()

    def draw(self):
        #self.screen.fill("gray")
        """
        self.screen.blit(self.background, self.coordBackground)
        self.screen.blit(self.background,
                         (self.coordBackground[0] + self.background.get_width(), self.coordBackground[1]))
                         """
        # Sol
        pygame.draw.line(self.screen, "white", (0, settings.GROUND_Y), (settings.SCREEN_WIDTH, settings.GROUND_Y), 5)

        # Joueur
        self.player.draw()
        self.player.draw_health_bar()

        # Obstacles
        for obs in self.obstacles:
            obs.draw(self.screen)

        #Plateforms
        for p in self.plateforms:
            p.draw(self.screen)

        # FPS
        fps_text = self.font.render(f"FPS: {int(self.clock.get_fps())}", True, pygame.Color("white"))
        self.screen.blit(fps_text, (10, 10))

        pygame.display.flip()

    def deffilerFond(self, vitesse):
        x, y = self.coordBackground
        x -= vitesse

        # si l'image est totalement sortie de l'écran, on la remet à 0
        if x <= -self.background.get_width():
            x = 0
        elif x >= self.background.get_width():
            x = 0

        self.coordBackground = (x, y)

    def run(self):
        while self.running:
            self.screen.fill((128, 128, 128))
            dt = self.clock.tick(settings.FPS) / 1000
            keys = pygame.key.get_pressed()
            self.handle_events()
            self.update(dt, keys)
            self.draw()
            """
            if self.player.state == "forward":
                self.deffilerFond(settings.PLAYER_SPEED*settings.PLAYER_PARALAX_EFFECT)
            elif self.player.state == "backward":
                self.deffilerFond(-settings.PLAYER_SPEED*settings.PLAYER_PARALAX_EFFECT)
            """

    def getListOfpLayer(self):
        return self.player_group.sprites()