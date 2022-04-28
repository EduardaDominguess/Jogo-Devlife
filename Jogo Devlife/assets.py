import pygame
import os
from configuracoes import *

 
BACKGROUND = 'background'
PREDIO = 'predio'
MOTO_BARBARA = 'moto_barbara'
MOTO_TOSHI = 'moto_toshi'
MOTO_FABRICIO = 'moto_fabricio'
MOTO_IGOR = 'moto_igor'
MOTO_GRAZI = 'moto_grazi'
MOTO_MIRANDA = 'moto_miranda'
BUTTON = 'button'
GETREADY = 'get_ready'
SCORE_FONT = 'score_font'
POINT_SOUND = 'point_sound'
SCORE_FONT = 'score_font'
TELAGAMEOVER = 'tela_gameover'



def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'fundo.png')).convert()   
    assets[BACKGROUND] = pygame.transform.scale(assets['background'], (WIDTH,HEIGHT))
    assets[PREDIO] = pygame.image.load(os.path.join(IMG_DIR, 'predio.png')).convert_alpha()
    assets[MOTO_BARBARA] = pygame.image.load(os.path.join(IMG_DIR, 'Barbara.png')).convert_alpha()
    assets[MOTO_BARBARA] = pygame.transform.scale(assets['moto_barbara'], (75, 75))
    assets[MOTO_TOSHI] = pygame.image.load(os.path.join(IMG_DIR, 'Toshi.png')).convert_alpha()
    assets[MOTO_TOSHI] = pygame.transform.scale(assets['moto_toshi'], (75, 75))
    assets[MOTO_FABRICIO] = pygame.image.load(os.path.join(IMG_DIR, 'Fabricio.png')).convert_alpha()
    assets[MOTO_FABRICIO] = pygame.transform.scale(assets['moto_fabricio'], (75, 75))
    assets[MOTO_IGOR] = pygame.image.load(os.path.join(IMG_DIR, 'IGOR.png')).convert_alpha()
    assets[MOTO_IGOR] = pygame.transform.scale(assets['moto_igor'], (75, 75))
    assets[MOTO_GRAZI] = pygame.image.load(os.path.join(IMG_DIR, 'Grazi.png')).convert_alpha()
    assets[MOTO_GRAZI] = pygame.transform.scale(assets['moto_grazi'], (75, 75))
    assets[MOTO_MIRANDA] = pygame.image.load(os.path.join(IMG_DIR, 'Miranda.png')).convert_alpha()
    assets[MOTO_MIRANDA] = pygame.transform.scale(assets['moto_miranda'], (75, 75))
    assets[BUTTON] = pygame.image.load(os.path.join(IMG_DIR, 'button.png')).convert()
    assets[GETREADY] = pygame.image.load(os.path.join(IMG_DIR, 'getready.png')).convert_alpha()
    assets[GETREADY] = pygame.transform.scale(assets['get_ready'], (600, 500))
    assets[TELAGAMEOVER] = pygame.image.load(os.path.join(IMG_DIR, 'telagameover.png')).convert()
    assets[TELAGAMEOVER] = pygame.transform.scale(assets['tela_gameover'], (WIDTH, HEIGHT))
    

    # Audios
    pygame.mixer.music.load(os.path.join(SND_DIR, 'soundtrack.mp3'))
    pygame.mixer.music.set_volume(0.4)
    assets[POINT_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'point.wav'))
    
    # Fonte
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 35)
    return 