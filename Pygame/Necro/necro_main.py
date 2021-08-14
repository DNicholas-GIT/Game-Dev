import pygame
import random
from sys import exit



pygame.init()
screen = pygame.display.set_mode((1600,1200))
pygame.display.set_caption('Necro')
clock = pygame.time.Clock()

test_font = pygame.font.SysFont('Arial', 75)
game_active = False


start_new_game = test_font.render(' New Game ', False, (161, 24, 14))
start_new_game_rect = start_new_game.get_rect(center = (800, 800))

player_char = pygame.image.load('graphics/gray circle.png').convert_alpha()
player_rect = player_char.get_rect(center = (800,600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active:
        screen.fill((11, 107, 54))
        screen.blit(player_char, player_rect)

        move_keys = pygame.key.get_pressed()
        if move_keys[pygame.K_w]:
            player_rect.y += -1
        if move_keys[pygame.K_s]:
            player_rect.y += 1
        if move_keys[pygame.K_a]:
            player_rect.x += -1
        if move_keys[pygame.K_d]:
            player_rect.x += 1


    else:
        screen.fill((71, 77, 74))
        pygame.draw.rect(screen,(42, 43, 42),start_new_game_rect)
        pygame.draw.rect(screen,'Black',start_new_game_rect, 6, 5)
        screen.blit(start_new_game, start_new_game_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_new_game_rect.collidepoint(event.pos):
                game_active = True




    pygame.display.update()
    clock.tick(45)