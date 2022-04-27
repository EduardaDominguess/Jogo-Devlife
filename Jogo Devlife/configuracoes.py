from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'audios')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fontes')

# Dados gerais do jogo.
WIDTH = 1024 # Largura da tela
HEIGHT = 768 # Altura da tela
FPS = 60 # Frames por segundo

# Define tamanhos
MOTO_WIDTH = 70
MOTO_HEIGHT = 70
GETREADY_WIDTH = 280
GETREADY_HEIGHT = 293


# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

