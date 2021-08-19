import pygame
from plat_tiles import Tile

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
    
    def setup_level(self, layout):
        self.plat_tiles = pygame.sprite.Group()
        for row in layout:
            print(row)


    def run(self):
        self.plat_tiles.draw(self.display_surface)