import pygame


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