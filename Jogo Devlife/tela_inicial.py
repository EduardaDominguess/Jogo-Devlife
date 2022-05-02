import pygame
import random
from os import path
from configuracoes import *


def init_screen(screen):
    #Velocidade
    clock = pygame.time.Clock()
    pygame.display.set_caption('Delivering Food')
    icon = pygame.image.load('./Assets/img/Toshi.png')
    pygame.display.set_icon(icon)
    background = pygame.image.load(path.join(IMG_DIR, 'First_screen.png')).convert_alpha()
    background_set = pygame.transform.scale(background, (WIDTH,HEIGHT))
    background_rect = background.get_rect()

    running = True
    while running:
        # Vel do jogo
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = ESCOLHA
                running = False
        # Redesenha o fundo 
        screen.fill(BLACK)
        screen.blit(background_set, background_rect)

        # Depois do desenho inverte o display 
        pygame.display.flip()

    return state 