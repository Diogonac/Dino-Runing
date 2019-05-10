"""
Insper
Authors: Diogo Nobre de Araujo Cintra, Luís Eduardo Satou Ferreira Pinheiro and Laura Batman Perim
Graduating in Mechanical Engineering, Mechatronical Engineering and Computer Engineering
Email: diogonac@al.insper.edu.br
Email: luisesfp@al.insper.edu.br
Email: laurabp@al.insper.edu.br
"""

# Importando as bibliotecas necessárias.
import pygame as pg
from os import path
import random

# Inicialização do Pygame.
pg.init()
pg.mixer.init()

WIDTH = 600 # Largura da tela
HEIGHT = 350 # Altura da tela
FPS = 60 # Frames por segundo
GRAVITY = 0.6

screen = pg.display.set_mode((WIDTH, HEIGHT))


pg.display.set_caption("Dino Run")
clock = pg.time.Clock()
background = pg.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()
player = Player()
all_sprites = pg.sprite.Group()
all_sprites.add(player)
img_dir = path.join(path.dirname(__file__), 'img')


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)



class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        player_img = pg.image.load(path.join(img_dir, "Dino.png")).convert()
        self.image = player_img
        self.image = pg.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedy = 0
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > HEIGHT:
            self.rect.y = HEIGHT
        if self.rect.y < 0:
            self.rect.y = 0
            




try: 
    # Loop principal.
    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pg.event.get():
            # Verifica se foi fechado.
            if event.type == pg.QUIT:
                running = False
            # Verifica se apertou alguma tecla.
            if event.type == pg.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pg.K_SPACE:
                    player.speedy = 11.5        
            # Verifica se soltou alguma tecla.
            if event.type == pg.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pg.K_SPACE:
                    player.speedy = 0
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        # Depois de desenhar tudo, inverte o display.
        pg.display.flip()
    

        
finally:
    pg.quit()
