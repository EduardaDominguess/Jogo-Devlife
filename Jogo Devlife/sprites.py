# Importando as bibliotecas necessárias.
import random
import pygame
from configuracoes import *
from assets import *


# Classe Jogador que representa os personagens
class moto(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/img/Barbara.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.pulo = False

    def update(self):
        # Gravity
        self.vel += 0.5
        if self.vel>8:
            self.vel = 8
        if self.rect.bottom<HEIGHT :
            self.rect.y += int(self.vel)

        # Jump
        if pygame.mouse.get_pressed()[0] == 1 and self.pulo == False:
            self.pulo = True
            self.vel = -10
        if pygame.mouse.get_pressed()[0] == 0 and self.pulo == False:
            self.pulo = False

        # Mantém dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    
class predio(pygame.sprite.Sprite):
    def __init__(self, x, y, posicao):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/img/predio.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        # Prédio vindo de cima
        if posicao == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.topleft = [x, y + int(400/2)]
        # Prédio vindo debaixo
        if posicao == -1:
            self.rect.bottomleft = [x, y + int(400/2)]

    def update(self):
        self.rect.x -= 4