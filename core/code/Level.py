import pygame
import os
import pymunk
from core.code.Tile import Tile
from pytmx.util_pygame import load_pygame

class Level:
    def __init__(self, screen, player, group, space):
        self.screen = screen
        self.player = player
        self.base_path = os.path.dirname(__file__)
        self.tmx_path = os.path.join(self.base_path, '../data/tmx/levelTest.tmx')
        self.tmxData = load_pygame(os.path.abspath(self.tmx_path))
        self.group = group

        self.space = space

        self.takeAllLayers()
        self.test()

    def takeAllLayers(self):
        for layer in self.tmxData.layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * 16, y * 16)
                    Tile(pos, surf, self.group)

    def test(self):
        for obj in self.tmxData.objects:
            pos = obj.x, obj.y
            if obj.type in ('Building', 'Vegetation'):
                Tile(pos, obj.image, self.group)

    def drawShapes(self):
        for obj in self.tmxData.objects:
            if obj.type == 'Shape' and obj.name == 'Marker':
                pos = (int(obj.x), int(obj.y))
                pygame.draw.circle(self.screen, 'red', pos, 25)
