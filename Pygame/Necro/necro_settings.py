import pygame
tile_size = 16
screen_width = 1600
screen_height = 1200


GRIDWIDTH = screen_width / tile_size
GRIDHEIGHT = screen_height / tile_size

game_title = ' Necro '



green_field = pygame.image.load('graphics/ground/biggreen.png').convert()
zoom_green_field = pygame.transform.scale(green_field, (int(green_field.get_width()*2), int(green_field.get_height()*2)))
