import pygame
import random
from os import path
from configuracoes import *


def init_screen(screen):
    # Variável para o ajustar velocidade
    clock = pygame.time.Clock()

    # Carrega tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'First_screen.png')).convert_alpha()
    background_set = pygame.transform.scale(background, (WIDTH,HEIGHT))
    background_rect = background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade.
        clock.tick(FPS)

        # ventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background_set, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state