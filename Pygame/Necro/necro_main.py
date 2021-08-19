import pygame
from random import randint
from sys import exit
# from dataclasses import dataclasses



pygame.init()
screen = pygame.display.set_mode((1600,1200))
pygame.display.set_caption('Necro')
clock = pygame.time.Clock()

title_font = pygame.font.SysFont('Arial', 300)
test_font = pygame.font.SysFont('Arial', 75)
game_active = False

green_field = pygame.image.load('graphics/ground/biggreen.png').convert()
zoom_green_field = pygame.transform.scale(green_field, (int(green_field.get_width()*2), int(green_field.get_height()*2)))

title = title_font.render(' Necro ', True, (255, 255, 255))
title_rect = title.get_rect(center = (800,400))

start_new_game = test_font.render(' New Game ', True, (161, 24, 14))
start_new_game_rect = start_new_game.get_rect(center = (800, 800))

# player_char = pygame.image.load('graphics/gray circle.png').convert_alpha()
# player_rect = player_char.get_rect(center = (800,600))

# red_char = pygame.image.load('graphics/red circle.png').convert_alpha()
# red_char_rect = red_char.get_rect(center = (600,600))

# blue_char = pygame.image.load('graphics/blue circle.png').convert_alpha()
# blue_char_rect = blue_char.get_rect(center = (600,560))
#
# white_char = pygame.image.load('graphics/white circle.png').convert_alpha()
# white_char_rect = white_char.get_rect(center = (600,640))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/gray circle.png').convert_alpha()
        self.rect = self.image.get_rect(center=(800, 600))

    def player_input(self):
        move_keys = pygame.key.get_pressed()
        if move_keys[pygame.K_w]:
            self.rect.y += -1
        if move_keys[pygame.K_s]:
            self.rect.y += 1
        if move_keys[pygame.K_a]:
            self.rect.x += -1
        if move_keys[pygame.K_d]:
            self.rect.x += 1

    def update(self):
        self.player_input()


class Soldier(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'red':
            self.image = pygame.image.load('graphics/red circle.png').convert_alpha()
            self.rect = self.image.get_rect(center=(1000, 400))
        elif type == 'blue':
            self.image = pygame.image.load('graphics/blue circle.png').convert_alpha()
            self.rect = self.image.get_rect(center=(600, 400))
        elif type == 'white':
            self.image = pygame.image.load('graphics/white circle.png').convert_alpha()
            self.rect = self.image.get_rect(center=(800, 700))





#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

red_soldier = pygame.sprite.Group()
red_soldier.add(Soldier('red'))

blue_soldier = pygame.sprite.Group()
blue_soldier.add(Soldier('blue'))

white_soldier = pygame.sprite.Group()
white_soldier.add(Soldier('white'))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active:
        screen.blit(green_field,(0,0))



        player.draw(screen)
        player.update()

        red_soldier.draw(screen)
        blue_soldier.draw(screen)
        white_soldier.draw(screen)

        # if event.type == pygame.MOUSEWHEEL:
        #     if event.key == pygame.BUTTON_WHEELUP:
        #         screen.blit(zoom_green_field,(0,0))
        #
        # if event.type == pygame.MOUSEWHEEL:
        #     if event.key == pygame.BUTTON_WHEELDOWN:
        #         screen.blit(green_field,(0,0))

        # screen.blit(player_char, player_rect)
        # screen.blit(red_char, red_char_rect)
        # screen.blit(blue_char, blue_char_rect)
        # screen.blit(white_char, white_char_rect)





    else:
        screen.fill((71, 77, 74))
        pygame.draw.rect(screen,(42, 43, 42),start_new_game_rect)
        pygame.draw.rect(screen,'Black',start_new_game_rect, 6, 5)
        screen.blit(start_new_game, start_new_game_rect)
        screen.blit(title, title_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_new_game_rect.collidepoint(event.pos):
                game_active = True




    pygame.display.update()
    clock.tick(50)