import pygame
import random
from sys import exit



pygame.init()
screen = pygame.display.set_mode((1600,1200))
pygame.display.set_caption('Necro')
clock = pygame.time.Clock()

test_font = pygame.font.SysFont('Arial', 75)
game_active = False


start_new_game = test_font.render('New Game', False, (161, 24, 14))
start_new_game_rect = start_new_game.get_rect(center = (800, 800))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    if game_active:
        screen.fill((11, 107, 54))
    else:
        screen.fill((71, 77, 74))
        screen.blit(start_new_game, start_new_game_rect)

    pygame.display.update()
    clock.tick(45)