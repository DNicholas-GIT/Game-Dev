import pygame

pygame.font.init()

tile_size = 16
screen_width = 1600
screen_height = 1200
screen = pygame.display.set_mode((screen_width,screen_height))

# GRIDWIDTH = screen_width / tile_size
# GRIDHEIGHT = screen_height / tile_size

title_font = pygame.font.SysFont('Arial', 300)
test_font = pygame.font.SysFont('Arial', 75)

start_new_game = test_font.render(' New Game ', True, (161, 24, 14))
start_new_game_rect = start_new_game.get_rect(center=(800, 800))

title = title_font.render(' Necro ', True, (255, 255, 255))
title_rect = title.get_rect(center=(800, 400))

game_title = ' Necro '



# green_field = pygame.image.load('graphics/ground/biggreen.png').convert()
# zoom_green_field = pygame.transform.scale(green_field, (int(green_field.get_width()*2), int(green_field.get_height()*2)))
