# Importando bibliotecas
import pygame
import random
from pygame.locals import *
from configuracoes import *
from assets import *


def game_screen(window):

    pygame.init()
    pygame.mixer.init()

    # Tela Principal
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Delivering Food')
    icon = pygame.image.load('Assets/img/Toshi.png')
    pygame.display.set_icon(icon)

    # Inicia assets 
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

    # Carrega os sons
    pygame.mixer.music.load('assets/audios/soundtrack.mp3')
    pygame.mixer.music.set_volume(0.3)
    assets['point_sound'] = pygame.mixer.Sound('assets/audios/point.wav')

    # Carrega fonte
    assets['score_font'] = pygame.font.Font(('assets/fontes/PressStart2P.ttf'), 28)

    # Define variáveis
    mov_fundo = 0 
    vel_fundo = 4 # Velocidade de movimentação do fundo
    voando = False
    game_over = False
    freq_predio = 1500 
    last_predio = pygame.time.get_ticks() - freq_predio
    score = 0 
    pass_predio = False

    # Função utilizada para desenhar o placar do jogo
    def draw_text(text, font, text_color, x, y):
        img = assets[SCORE_FONT].render(text, True, text_color)
        window.blit(img, (x, y))

    # Função utilizada para dar reset no jogo
    def restart():
        predio_group.empty()
        p.rect.x = 200
        p.rect.y = int(HEIGHT / 2)
        score = 0
        return score


    # DEFINE CLASSES
    class moto(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = assets['moto_barbara']
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.vel = 0
            self.click = False
        
        def update(self):
            
            # Gravidade
            if voando == True:
                self.vel += 0.5
                if self.vel > 8 :
                    self.vel = 8
                if self.rect.bottom < 768:
                    self.rect.y += int(self.vel)

            if game_over == False:
                # Pular
                if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                    self.click = True
                    self.vel = -10
                if pygame.mouse.get_pressed()[0] == 0:
                    self.click = False

    # Criando grupos de sprite para o player
    sailor_group = pygame.sprite.Group()

    # Instância do player(posição na tela
    p = moto(200, int(HEIGHT / 2))
    sailor_group.add(p)

    class predio(pygame.sprite.Sprite):
        def __init__(self, x, y, posicao):
            pygame.sprite.Sprite.__init__(self)
            self.image = assets['predio']
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()

            # A posição 1 equivale ao predio vindo de cima 
            if posicao == 1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.rect.bottomleft = [x, y]
            # A posição -1 equivale  ao predio vindo de baixo
            if posicao == -1:
                self.rect.topleft = [x, y]
        
        def update(self):
            self.rect.x -= vel_fundo

            # Tira os prédios que já passaram pela tela
            if self.rect.right < 0:
                self.kill() 

    # Criando grupos de sprite para os prédios
    predio_group = pygame.sprite.Group()

    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        def draw(self):
            action = False
            
            # Ver a posição do mouse
            posicao = pygame.mouse.get_pos()

            # Checa se o mouse está em cima do botão
            if self.rect.collidepoint(posicao):
                if pygame.mouse.get_pressed()[0] == 1: # Botão esquerda do mouse foi pressionado
                    action = True

            # Desenha botão
            window.blit(self.image, (self.rect.x, self.rect.y))
            return action

    # Instânica do botão de restart(posição na tela e imagem)
    button = Button((WIDTH / 2) - 50, (HEIGHT / 2) - 100, assets['button'])



    game = True

    # Define os frames por segundo
    clock = pygame.time.Clock()
    FPS = 60

    # Toca a música do jogo
    pygame.mixer.music.play(loops=-1)
    # loop principal 
    while game:

        clock.tick(FPS)

        # Saídas 
        window.blit(assets['background'], (mov_fundo, 0)) # Desenha o fundo

        predio_group.draw(window) # Desenha o prédio    

        sailor_group.draw(window) # Desenha o personagem
        sailor_group.update() # Atualiza o que acontece com a moto
        
        # Verifica o Placar
        if len(predio_group) > 0:
            if sailor_group.sprites()[0].rect.left > predio_group.sprites()[0].rect.left\
                and sailor_group.sprites()[0].rect.right < predio_group.sprites()[0].rect.right and pass_predio == False:
                pass_predio = True
            if pass_predio == True:
                if sailor_group.sprites()[0].rect.left > predio_group.sprites()[0].rect.right:
                    score += 1
                    assets['point_sound'].play()
                    pass_predio = False

        # Desenha o placar na tela
        draw_text(str(score), assets['score_font'], WHITE, int(WIDTH / 2), 20)

        # Checa se a moto bateu no prédio ou nos limites da tela superior
        if pygame.sprite.groupcollide(sailor_group, predio_group, False, False) or p.rect.top < 0: # Os bol indicam que algum dos grupos seria deletado caso fosse atingido
            game_over = True

        # Checa se a moto bateu nos limites da tela inferior
        if p.rect.bottom >= 768:
            game_over = True
            voando = False

        # Checa se o jogo ainda não acabou
        if game_over == False and voando == True: 
            # Gerar novos prédios
            time_now = pygame.time.get_ticks()
            if time_now - last_predio > freq_predio:
                altura_canhao = random.randint(-100, 100)
                canhao_baixo = predio(WIDTH, 468 + altura_canhao, -1) # 488
                canhao_cima = predio(WIDTH, 260 + altura_canhao, 1) # 280
                predio_group.add(canhao_baixo)
                predio_group.add(canhao_cima)
                last_predio = time_now

            # movimentação do fundo
            mov_fundo -= vel_fundo 
            if abs(mov_fundo) > 2048:
                mov_fundo = 0   

            # Atualiza o que acontece com os prédios
            predio_group.update()

        # Desenha o get ready quando o jogo está ativo porém ainda não começou(voando é Falso)
        if game_over == False and voando == False:
            window.blit(assets['get_ready'], (400, 215))                             

        # Checa por game over e restart
        if game_over == True:
            window.blit(assets['tela_gameover'], (0,0)) # Desenha a tela de game over
            draw_text(str(score), assets['score_font'], WHITE, int(WIDTH/2) + 160, 708) # Desenha o placar na tela de game over
            if button.draw() == True: # O botão foi apertado
                game_over = False
                score = restart()

        # Tratamento de eventos para definir se o jogo deve acabar e se a moto deve começar a voar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN and voando == False and game_over == False:
                voando = True
        

        pygame.display.update()

    pygame.quit
