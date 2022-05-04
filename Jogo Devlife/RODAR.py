# Importando as bibliotecas necessárias.
import pygame
from configuracoes import * 
from tela_jogo import *
from tela_selecao import tela_selecao

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Delivering Food')

state = INIT
while state != QUIT:
    if state == ESCOLHA:
        state, personagem = tela_selecao(window)
    elif state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window, personagem)
    else:
        state = QUIT

pygame.quit()  