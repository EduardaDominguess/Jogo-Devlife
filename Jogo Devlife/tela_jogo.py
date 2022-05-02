# Importando bibliotecas
import pygame
import random
from pygame.locals import *
from configuracoes import *
from assets import *
from tela_selecao import *


def game_screen(window, personagem):

    pygame.init()
    pygame.mixer.init()

    # Tela Principal
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Delivering Food')
    icon = pygame.image.load('./Assets/img/Toshi.png')
    pygame.display.set_icon(icon)

    assets = {}
    assets['background'] = pygame.image.load('assets/img/fundo.png').convert()
    assets['moto_barbara'] = pygame.image.load('Assets/img/Barbara.png').convert_alpha()
    assets['moto_barbara'] = pygame.transform.scale(assets['moto_barbara'], (70, 70))
    assets['moto_toshi'] = pygame.image.load('Assets/img/Toshi.png').convert_alpha()
    assets['moto_toshi'] = pygame.transform.scale(assets['moto_toshi'], (70, 70))
    assets['moto_fabricio'] = pygame.image.load('Assets/img/Fabricio.png').convert_alpha()
    assets['moto_fabricio'] = pygame.transform.scale(assets['moto_fabricio'], (70, 70))
    assets['moto_igor'] = pygame.image.load('Assets/img/Igor.png').convert_alpha()
    assets['moto_igor'] = pygame.transform.scale(assets['moto_igor'], (70, 70))
    assets['moto_grazi'] = pygame.image.load('Assets/img/Grazi.png').convert_alpha()
    assets['moto_grazi'] = pygame.transform.scale(assets['moto_grazi'], (70, 70))
    assets['moto_miranda'] = pygame.image.load('Assets/img/Miranda.png').convert_alpha()
    assets['moto_miranda'] = pygame.transform.scale(assets['moto_miranda'], (70, 70))
    assets['predio'] = pygame.image.load('assets/img/predio.png').convert_alpha()
    assets['button'] = pygame.image.load('assets/img/button.png')
    assets['get_ready'] = pygame.image.load('assets/img/getready.png').convert_alpha()
    assets['get_ready'] = pygame.transform.scale(assets['get_ready'], (210, 223))
    assets['tela_gameover'] = pygame.image.load('assets/img/telagameover.png').convert()
    assets['tela_gameover'] = pygame.transform.scale(assets['tela_gameover'], (WIDTH, HEIGHT))

    # Audios
    pygame.mixer.music.load('assets/audios/soundtrack.mp3')
    pygame.mixer.music.set_volume(0.3)
    assets['point_sound'] = pygame.mixer.Sound('assets/audios/point.wav')

    # Fonte
    assets['score_font'] = pygame.font.Font(('assets/fontes/PressStart2P.ttf'), 28)

    mov_fundo = 0 
    vel_fundo = 4 
    voando = False
    game_over = False
    freq_predio = 1500 
    last_predio = pygame.time.get_ticks() - freq_predio
    score = 0 
    pass_predio = False

    # Placar 
    def draw_text(text, font, text_color, x, y):
        img = assets[SCORE_FONT].render(text, True, text_color)
        window.blit(img, (x, y))

    # Resetar
    def restart():
        predio_group.empty()
        p.rect.x = 200
        p.rect.y = int(HEIGHT / 2)
        score = 0
        return score


    class moto(pygame.sprite.Sprite):
        def __init__(self, x, y, professor):
            pygame.sprite.Sprite.__init__(self)
            self.image = assets[professor]
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.vel = 0
            self.click = False
        
        def update(self):
            
            # Gravity
            if voando == True:
                self.vel += 0.5
                if self.vel > 8 :
                    self.vel = 8
                if self.rect.bottom < 768:
                    self.rect.y += int(self.vel)

            if game_over == False:
                # Jump
                if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                    self.click = True
                    self.vel = -10
                if pygame.mouse.get_pressed()[0] == 0:
                    self.click = False


    moto_group = pygame.sprite.Group()

    # Posição na tela
    p = moto(200, int(HEIGHT / 2), personagem)
    moto_group.add(p)

    class predio(pygame.sprite.Sprite):
        def __init__(self, x, y, posicao):
            pygame.sprite.Sprite.__init__(self)
            self.image = assets['predio']
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()

            # Vindo de cima 
            if posicao == 1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.rect.bottomleft = [x, y]
            # Vindo de baixo
            if posicao == -1:
                self.rect.topleft = [x, y]
        
        def update(self):
            self.rect.x -= vel_fundo

            # Tira os prédios que já passaram pela tela
            if self.rect.right < 0:
                self.kill() 

    predio_group = pygame.sprite.Group()

    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        def draw(self):
            action = False
            
            posicao = pygame.mouse.get_pos()

            if self.rect.collidepoint(posicao):
                if pygame.mouse.get_pressed()[0] == 1: 
                    action = True


            window.blit(self.image, (self.rect.x, self.rect.y))
            return action

    button = Button((WIDTH / 2) - 50, (HEIGHT / 2) - 100, assets['button'])



    game = True

    clock = pygame.time.Clock()
    FPS = 60

    pygame.mixer.music.play(loops=-1)
    while game:

        clock.tick(FPS)

        window.blit(assets['background'], (mov_fundo, 0)) # Fundo

        predio_group.draw(window) # Prédio    

        moto_group.draw(window) #Personagem
        moto_group.update() 
        
        # Pontos
        if len(predio_group) > 0:
            if moto_group.sprites()[0].rect.left > predio_group.sprites()[0].rect.left\
                and moto_group.sprites()[0].rect.right < predio_group.sprites()[0].rect.right and pass_predio == False:
                pass_predio = True
            if pass_predio == True:
                if moto_group.sprites()[0].rect.left > predio_group.sprites()[0].rect.right:
                    score += 1
                    assets['point_sound'].play()
                    pass_predio = False

        # Pontos na tela
        draw_text(str(score), assets['score_font'], WHITE, int(WIDTH / 2), 20)

        if pygame.sprite.groupcollide(moto_group, predio_group, False, False) or p.rect.top < 0: 
            game_over = True

        if p.rect.bottom >= 768:
            game_over = True
            voando = False

        if game_over == False and voando == True: 
            # New prédios
            time_now = pygame.time.get_ticks()
            if time_now - last_predio > freq_predio:
                altura_canhao = random.randint(-100, 100)
                canhao_baixo = predio(WIDTH, 468 + altura_canhao, -1) 
                canhao_cima = predio(WIDTH, 260 + altura_canhao, 1) 
                predio_group.add(canhao_baixo)
                predio_group.add(canhao_cima)
                last_predio = time_now

            mov_fundo -= vel_fundo 
            if abs(mov_fundo) > 2048:
                mov_fundo = 0   

            predio_group.update()

        if game_over == False and voando == False:
            window.blit(assets['get_ready'], (400, 215))                             

        if game_over == True:
            window.blit(assets['tela_gameover'], (0,0)) 
            draw_text(str(score), assets['score_font'], WHITE, int(WIDTH/2) + 160, 708) 
            if button.draw() == True: 
                game_over = False
                score = restart()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN and voando == False and game_over == False:
                voando = True
        

        pygame.display.update()

    pygame.quit