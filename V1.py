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
vec = pg.math.Vector2

# Inicialização do Pygame.
pg.init()
pg.mixer.init()

WIDTH = 600 # Largura da tela
HEIGHT = 350 # Altura da tela
FPS = 60 # Frames por segundo
GRAVITY = 0.6

BLACK = (0,0,0)
WHITE = (255,255,255)

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        player_img = pg.image.load(path.join(img_dir, "Dino.png")).convert()
        self.image = player_img
        self.image = pg.transform.scale(player_img, (100, 100))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 25
        self.speedy = -12
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > HEIGHT:
            self.rect.y = HEIGHT
        if self.rect.y < 0:
            self.rect.y = 0
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC    
        
            

class Mob(pg.sprite.Sprite):
    #construtor da classe
    def __init__(self, px, py):
        #construtor classe pai
        pg.sprite.Sprite.__init__(self)
        #carregando imagem de fundo
        mob_img = pg.image.load(path.join(img_dir, "cacto.png")).convert()
        self.image = mob_img
        #diminuindo tamanho da imagem
        self.image = pg.transform.scale(mob_img, (40, 32))
        #detalhes posicao
        self.rect=self.image.get_rect()
        #sorteia lugar inicial em x
        self.rect.x=px
        #sorteia lugar y
        self.rect.y=py
        #sorteia velocidade inicial
        self.speedx= 0
        self.speedy= -3



        self.image.set_colorkey(WHITE)
         
        #Mob_rect1.x -=3              
        #background_rect2.x -=3
        #screen.blit(background, background_rect1)
        #screen.blit(background, background_rect2)
        #if background_rect1.x<0:
         ##   background_rect2.x = 0

    def update(self):
        self.rect.x += self.speedy

        
        #se as plantas passarem da tela volta para o lado
        if self.rect.top>HEIGHT + 10 or self.rect.left < -25 or  self.rect.right > WIDTH + 20:
           self.rect.x = 20
           self.rect.y= -20
           self.rect.bottom=295
           self.rect.centerx = WIDTH 
           
      
         
             
   
            
           
           
            

screen = pg.display.set_mode((WIDTH, HEIGHT))
img_dir = path.join(path.dirname(__file__), 'img')


pg.display.set_caption("Dino Run")
clock = pg.time.Clock()

# carregue a imagem do fundo e coloque no background
background = pg.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect1 = background.get_rect()
background_rect2 = background.get_rect()
background_rect1.x = WIDTH

player = Player()
all_sprites = pg.sprite.Group()
all_sprites.add(player)

mob = pg.sprite.Group()
for i in range(4):
    mobs = Mob(random.randint(1, WIDTH), 260)
    all_sprites.add(mob)
    mob.add(mobs)

    
    

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)



# Tamanho da tela.
screen = pg.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pg.display.set_caption("Dino Run")

# Variável para o ajuste de velocidade
clock = pg.time.Clock()



try: 
    # Loop principal.
    running = True
    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    player.speedy = -10       
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    player.speedy = 0
        all_sprites.update()
        screen.fill(BLACK)
        


        
       
        background_rect1.x -=3              
        background_rect2.x -=3
        screen.blit(background, background_rect1)
        screen.blit(background, background_rect2)
        if background_rect1.x<0:
            background_rect1.x = WIDTH
            background_rect2.x = 0
      
        
#x negatico é fora da tela         
        print(background_rect1.x)
        
        all_sprites.draw(screen)
        # Depois de desenhar tudo, inverte o display.
        pg.display.flip()
    

        
finally:
    pg.quit()
