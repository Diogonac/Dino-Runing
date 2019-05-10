"""
Insper
Authors: Diogo Nobre de Araujo Cintra, Luís Eduardo Satou Ferreira Pinheiro and Laura Batman Perim
Graduating in Mechanical Engineering, Mechatronical Engineering and Computer Engineering
Email: diogonac@al.insper.edu.br
Email: luisesfp@al.insper.edu.br
Email: laurabp@al.insper.edu.br
"""

# Importando as bibliotecas necessárias.
import pygame
import random
import time
from os import path

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
WIDTH = 600 # Largura da tela
HEIGHT = 350 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Classe Jogador que representa a nave
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "Dino.png")).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 38))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        
        self.speedy = 0
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.space > HEIGHT:
            self.rect.space = HEIGHT
        if self.rect.space < 0:
            self.rect.space = 0
            


class Mob(pygame.sprite.Sprite):
    #construtor da classe
    def __init__(self):
        #construtor classe pai
        pygame.sprite.image.sprite.__init__(self)
        #carregando imagem de fundo
        player_img = pygame.image.load(path.join(img_dir, "layerShip1_orangpe.png")).convert()
        self.image = player_img
        #diminuindo tamanho da imagem
        self.image = pygame.transform.scale(player_img, (40, 32))
        #detalhes posicao
        self.rect=self.image.get_rect()
        #sorteia lugar inicial em x
        self.rect.x=random.randrange(WIDTH - self.rect.width)
        #sorteia lugar y
        self.rect.y=random.randrange(WIDTH - self.rect.width)
        #sorteia velocidade inicial
        self.speedx=random.randrange(1,5)
        self.speedy=random.randrange(-1,1)
        #se as plantas passarem da tela volta para o lado
        if self.rect.top>HEIGHT + 10 or self.rect.left < -25 or  self.rect.righ > WIDTH + 20:
           self.rect.x = random. randrange (WIDTH - self.rect.width)
           self.rect.y=random. randrange (-100, -40)
           self.speedx = random.randrange(-3, 3)
           self.speedy = random.randrange(2, 9)
            
            
# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
<<<<<<<HEAD
pygame.display.set_caption("Dino")
=======
pygame.display.set_caption("Dino Run")
>>>>>>> abfd79d13336e2087391a6530ae9ac5d600df083

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()


# Cria uma nave. O construtor será chamado automaticamente.
player = Player()

# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Comando para evitar travamentos.
try:
    
    # Loop principal.
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False
            
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.SPACE:
                    player.speedy = 10
                    
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.SPACE:
                    player.speedy = 0
            
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
            
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    

        
finally:
    pygame.quit()
