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

BLACK = (0,0,0)
WHITE = (255,255,255)

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        player_img = pg.image.load(path.join(img_dir, "Dino.png")).convert()
        self.image = player_img
        self.image = pg.transform.scale(player_img, (30, 30))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT -50
        self.speedy = 0
        self.pulando = False
        
    def update(self):
        self.rect.y += self.speedy
        self.speedy += GRAVITY


        if self.rect.y > HEIGHT:
            self.speedy = 0
            self.rect.y = HEIGHT
        if self.rect.y < 0:
            self.speedy = 0
            self.rect.y = 0
        
   

        if self.rect.bottom > HEIGHT - 50:
            self.rect.bottom = HEIGHT - 55
            self.pulando = False
            
#        if self.rect.y > HEIGHT:
#            self.rect.y = HEIGHT
#        if self.rect.y < 0:
#            self.rect.y = 0
            

        
            

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

    def update(self):
        self.rect.x += self.speedy

class Vida(pg.sprite.Sprite):
    #construtor da classe
    def __init__(self, px, py):
        #construtor classe pai
        pg.sprite.Sprite.__init__(self)
        #carregando imagem de fundo
        mob_img = pg.image.load(path.join(img_dir, "coracao.png")).convert()
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

        self.image.set_colorkey(BLACK)

    def update(self):
        self.rect.x += self.speedy
        
class Aguia(pg.sprite.Sprite):
    #construtor da classe
    def __init__(self, px, py):
        #construtor classe pai
        pg.sprite.Sprite.__init__(self)
        #carregando imagem de fundo
        mob_img = pg.image.load(path.join(img_dir, "aguia.png")).convert()
        self.image = mob_img
        self.image.set_colorkey(BLACK)
        #diminuindo tamanho da imagem
        self.image = pg.transform.scale(mob_img, (40, 30))
        #detalhes posicao
        self.rect=self.image.get_rect()
        #sorteia lugar inicial em x
        self.rect.x=px
        #sorteia lugar y
        self.rect.y=py
 
        #sorteia velocidade inicial

        self.speedx= 0
        self.speedy= -3
        
    def update(self):
        
        self.rect.x += self.speedx
        
screen = pg.display.set_mode((WIDTH, HEIGHT))
img_dir = path.join(path.dirname(__file__), 'img')


pg.display.set_caption("Dino Run")
clock = pg.time.Clock()

# carregue a imagem do fundo e coloque no background
background = pg.image.load(path.join(img_dir, 'starfield.png')).convert()
TI = pg.image.load(path.join(img_dir, 'telainicial.png')).convert()           
TF = pg.image.load(path.join(img_dir, 'telainicial.png')).convert()  

background_rect1 = background.get_rect()
background_rect2 = background.get_rect()
background_rect1.x = WIDTH

player = Player()
all_players = pg.sprite.Group()
all_players.add(player)

all_sprites = pg.sprite.Group()
all_sprites.add(player)

all_mobs = pg.sprite.Group()
all_aguias=pg.sprite.Group()
all_vida=pg.sprite.Group()
#for i in range(1):
#    mob = Mob(WIDTH, 260)
#    all_sprites.add(mob)
#    all_mobs.add(mob)
#
    
    

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
prob_vida = random.randint(60,10000) 

cont_Mob = 0
intervalo_Mob = random.randint(FPS//2, 3*FPS)
cont_aguia=0
intervalo_aguia = random.randint(FPS//2, 3*FPS)
cont_life=0
intervalo_life = random.randint(FPS//2, 3*FPS)


try: 

    # Loop principal.
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    running = False

        screen.blit(TI, TI.get_rect())
        pg.display.flip()
    

    
    running = True
    while running:
        clock.tick(FPS)

        if cont_Mob == intervalo_Mob:
            mob = Mob(WIDTH, 260)
            all_sprites.add(mob)
            all_mobs.add(mob)
            cont_Mob = 0
            intervalo_Mob = random.randint(FPS//2, FPS)

        if cont_aguia == intervalo_aguia:
            aguia = Aguia(WIDTH, 235)
            aguia.speedx -= 5
            all_sprites.add(aguia)
            all_aguias.add(aguia)
            cont_aguia = 0
            intervalo_aguia = random.randint(FPS//2, FPS)            
            
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if not player.pulando:
                        player.pulando = True
                        player.speedy = -11 
            #if event.type == pg.KEYUP: 
                #if event.key == pg.K_SPACE:
                    
                    
        all_sprites.update()
        screen.fill(BLACK)
        
        hits = pg.sprite.groupcollide(all_players, all_mobs,False, True)
        if hits:
           running = False #pass
            #running = False
        cont_Mob += 1
        cont_aguia+=1
        cont_life+=1
               
        background_rect1.x -=3              
        background_rect2.x -=3
        screen.blit(background, background_rect1)
        screen.blit(background, background_rect2)
        if background_rect1.x<0:
            background_rect1.x = WIDTH
            background_rect2.x = 0
      
        
#x negatico é fora da tela 
        
        if cont_life == prob_vida:
            vida = Vida(WIDTH, 260)
            all_sprites.add(vida)
            all_vida.add(vida)
            cont_life = 0
            prob_life = random.randint(240,1000)
            

        
        all_sprites.draw(screen)
        # Depois de desenhar tudo, inverte o display.
        pg.display.flip()
    
    
    running = True
    while running:
        clock.tick(FPS)
        screen.blit(TI, TI.get_rect())
        pg.display.flip()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                running = True 

                    


        
finally:
    pg.quit()
