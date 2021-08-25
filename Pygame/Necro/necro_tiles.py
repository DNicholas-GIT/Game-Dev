import pygame
from necro_settings import *





class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())


            self.tilewidth = len(self.data[0])
            self.tileheight = len(self.data)
            self.width = self.tilewidth * tile_size
            self.height = self.tileheight * tile_size

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(screen_width /2)
        y = -target.rect.y + int(screen_height /2)


        # Limit scrolling
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - screen_width), x)
        y = max(-(self.height - screen_height), y)
        self.camera = pg.Rect(x, y, self.width, self.height)