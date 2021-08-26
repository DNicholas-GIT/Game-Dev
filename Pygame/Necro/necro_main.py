import pygame
import sys
from necro_settings import *
from necro_level import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(game_title)
        self.clock = pygame.time.Clock()
        self.game_active = False

    def update(self):
        self.clock.tick(60)
        self.screen.fill(0)
        self.transition()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def transition(self):

        if not self.game_active:
            self.start_menu()
        else:
            self.level()

    def start_menu(self):

            screen.fill((71, 77, 74))
            pygame.draw.rect(screen, (42, 43, 42), start_new_game_rect)
            pygame.draw.rect(screen, 'Black', start_new_game_rect, 6, 5)

            screen.blit(start_new_game, start_new_game_rect)
            screen.blit(title, title_rect)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_new_game_rect.collidepoint(event.pos):
                        print("menu")
                        self.game_active = True

    def level(self):
        green_field = pygame.image.load('graphics/ground/biggreen.png').convert()
        screen.blit(green_field, (0, 0))


game = Game()

while True:
    game.update()
    pygame.display.update()



