import pygame
import random
from os import path
from pygame.locals import *
from configuracoes import *
from assets import *

#função que detecta colisão do mouse com a imagem
def colisao(ponto, r2):
    return r2.collidepoint(ponto)


def tela_selecao(screen: pygame.Surface):
    pygame.init()
    pygame.display.set_caption('Delivering Food')
    icon = pygame.image.load('./Assets/img/Toshi.png')
    pygame.display.set_icon(icon)

    assets = {}
    assets['moto_barbara'] = pygame.image.load('Assets/img/Barbara.png').convert_alpha()
    assets['moto_barbara'] = pygame.transform.scale(assets['moto_barbara'], (150, 150))
    assets['moto_toshi'] = pygame.image.load('Assets/img/Toshi.png').convert_alpha()
    assets['moto_toshi'] = pygame.transform.scale(assets['moto_toshi'], (150, 150))
    assets['moto_fabricio'] = pygame.image.load('Assets/img/Fabricio.png').convert_alpha()
    assets['moto_fabricio'] = pygame.transform.scale(assets['moto_fabricio'], (150, 150))
    assets['moto_igor'] = pygame.image.load('Assets/img/Igor.png').convert_alpha()
    assets['moto_igor'] = pygame.transform.scale(assets['moto_igor'], (150, 150))
    assets['moto_grazi'] = pygame.image.load('Assets/img/Grazi.png').convert_alpha()
    assets['moto_grazi'] = pygame.transform.scale(assets['moto_grazi'], (150, 150))
    assets['moto_miranda'] = pygame.image.load('Assets/img/Miranda.png').convert_alpha()
    assets['moto_miranda'] = pygame.transform.scale(assets['moto_miranda'], (150, 150))
    assets['moto_marcos'] = pygame.image.load('Assets/img/Marcos.png').convert_alpha()
    assets['moto_marcos'] = pygame.transform.scale(assets['moto_marcos'], (150, 150))

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    background = pygame.image.load(path.join(IMG_DIR, 'Choose.png')).convert_alpha()
    background_set = pygame.transform.scale(background, (WIDTH,HEIGHT))
    background_rect = background.get_rect()
    screen.blit(assets['moto_barbara'],(200,300))
    screen.blit(assets['moto_toshi'],(400,300))
    screen.blit(assets['moto_miranda'],(600,300))
    screen.blit(assets['moto_grazi'],(200,450))
    screen.blit(assets['moto_fabricio'],(400,450))
    screen.blit(assets['moto_igor'],(600,450))
    screen.blit(assets['moto_igor'],(700,350))


    running = True
    while running:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and colisao(mouse,Rect(200,300,150,150)) == True:
                state = GAME
                personagem = 'moto_barbara'
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and colisao(mouse,Rect(400,300,150,150)) == True:
                state = GAME
                personagem = 'moto_toshi'
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and colisao(mouse,Rect(600,300,150,150)) == True:
                state = GAME
                personagem = 'moto_miranda'
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and colisao(mouse,Rect(200,450,150,150)) == True:
                state = GAME
                personagem = 'moto_grazi'
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and colisao(mouse,Rect(400,450,150,150)) == True:
                state = GAME
                personagem = 'moto_fabricio'
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and colisao(mouse,Rect(600,450,150,150)) == True:
                state = GAME
                personagem = 'moto_igor'
                running = False

        screen.blit(background_set, background_rect)
        screen.blit(assets['moto_barbara'],(200,300))
        screen.blit(assets['moto_toshi'],(400,300))
        screen.blit(assets['moto_miranda'],(600,300))
        screen.blit(assets['moto_grazi'],(200,450))
        screen.blit(assets['moto_fabricio'],(400,450))
        screen.blit(assets['moto_igor'],(600,450))
        screen.blit(assets['moto_marcos'],(800,400))

        pygame.display.flip()

    return state, personagem