from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'audios')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fontes')

WIDTH = 1024 
HEIGHT = 768 
FPS = 60 # Frames por segundo

MOTO_WIDTH = 70
MOTO_HEIGHT = 70
GETREADY_WIDTH = 280
GETREADY_HEIGHT = 293

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

INIT = 0
GAME = 1
QUIT = 2