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
        self.pnjDict = {}

        self.space = space

        self.takeAllLayers()
        self.takeAllObjects()
        self.shapes()

    def setPlayer(self, player):
        self.player = player

    def addPnj(self, pnj):
        self.pnjDict[pnj.name] = [pnj, pnj.pos, (pnj.x, pnj.y)]
        for obj in self.tmxData.objects:
            if obj.type == 'PnjMarker':
                self.pnjDict[obj.name][1] = (obj.x, obj.y)
                self.pnjDict[obj.name][0].setPos((obj.x, obj.y))
            if obj.type == 'pnjDetectDialog':
                 self.pnjDict[obj.name][2] = (obj.x, obj.y)

    def takeAllLayers(self):
        for layer in self.tmxData.layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * 16, y * 16)
                    Tile(pos, surf, self.group, self.space)


    def takeAllObjects(self):
        for obj in self.tmxData.objects:
            pos = obj.x, obj.y
            if obj.type in ('Building', 'Vegetation'):
                Tile(pos, obj.image, self.group, self.space)

    def shapes(self):
        for obj in self.tmxData.objects:
            if obj.type == 'Marker':
                if obj.name == 'SpawnPoint':
                    self.spawnPoint = (obj.x, obj.y)


