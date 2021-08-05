import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

text_score_surface = test_font.render(' Runner', False, 'Red')
text_score_rect = text_score_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (700,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print("collide")

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))

    pygame.draw.line(screen, 'Black', (0,0), pygame.mouse.get_pos(), 2)

    pygame.draw.rect(screen, 'Black', text_score_rect)
    pygame.draw.rect(screen, 'Black', text_score_rect, 10)
    screen.blit(text_score_surface,text_score_rect)


    snail_rect.x -= 4
    if snail_rect.x <= -100: snail_rect.left = 850
    screen.blit(snail_surface, snail_rect)

    screen.blit(player_surface, player_rect)

    if player_rect.colliderect(snail_rect):
        print("You died")
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     pygame.mouse.get_pressed()

    pygame.display.update()
    clock.tick(45)
