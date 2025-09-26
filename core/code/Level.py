import pygame
import os
from core.code.Tiles.Tile import Tile
from pytmx.util_pygame import load_pygame

class Level:
    def __init__(self, screen, group, space, player = None):
        self.screen = screen
        self.player = player
        self.base_path = os.path.dirname(__file__)
        self.tmx_path = os.path.join(self.base_path, '../data/tmx/levelTest.tmx')
        self.tmxData = load_pygame(os.path.abspath(self.tmx_path))
        self.group = group
        self.spawnPoint = (0, 0)

        self.space = space

        self.takeAllLayers()
        self.test()
        self.shapes()

    def setPlayer(self, player):
        self.player = player

    def takeAllLayers(self):
        for layer in self.tmxData.layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * 16, y * 16)
                    Tile(pos, surf, self.group, self.space)


    def test(self):
        for obj in self.tmxData.objects:
            pos = obj.x, obj.y
            if obj.type in ('Building', 'Vegetation'):
                Tile(pos, obj.image, self.group, self.space)

    def shapes(self):
        for obj in self.tmxData.objects:
            print(obj.type , obj.name)
            if obj.type == 'Marker' and obj.name == 'SpawnPoint':
                print(self.spawnPoint)
                self.spawnPoint = (obj.x, obj.y)
                print(self.spawnPoint)


