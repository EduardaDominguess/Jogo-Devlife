
import pygame
from configuracoes import WIDTH, HEIGHT, INIT, GAME, QUIT
from tela_inicial import init_screen
from tela_jogo import game_screen


pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Delivering Food')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    else:
        state = QUIT

pygame.quit()  
