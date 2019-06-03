"""
Insper
Authors: Diogo Nobre de Araujo Cintra, Luís Eduardo Satou Ferreira Pinheiro and Laura Batman Perim
Graduating in Mechanical Engineering, Mechatronical Engineering and Computer Engineering
Email: diogonac@al.insper.edu.br
Email: luisesfp@al.insper.edu.br
Email: laurabp@al.insper.edu.br
"""
import pygame as pg
from os import path
import random
from os import path
fnt_dir = path.join(path.dirname(__file__), 'font')
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
pg.init()
pg.mixer.init()
WIDTH = 600 
HEIGHT = 350 
FPS = 60 
GRAVITY = 0.6
velocidade = 3
BLACK = (0,0,0)
WHITE = (255,255,255)

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.imgs = {}
        self.imgs[0] = pg.transform.scale(pg.image.load(path.join(img_dir,"Dino1.png")).convert(), (30, 30))
        self.imgs[1] = pg.transform.scale(pg.image.load(path.join(img_dir,"Dino2.png")).convert(), (30, 30))
        self.imgs[0].set_colorkey(WHITE)
        self.imgs[1].set_colorkey(WHITE)
        self.img_index = 0
        self.image = self.imgs[self.img_index]
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT -50 
        self.speedy = 0
        self.pulando = False
        self.vida=3
        
    def update(self):
        self.image = self.imgs[self.img_index]
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
        
class Mob(pg.sprite.Sprite):
    #construtor da classe
    def __init__(self, px, py):
        pg.sprite.Sprite.__init__(self)
        mob_img = pg.image.load(path.join(img_dir, "cacto.png")).convert()
        self.image = mob_img
        self.image = pg.transform.scale(mob_img, (40, 32))
        self.rect=self.image.get_rect()
        self.rect.x=px
        self.rect.y=py
        self.speedx= -velocidade
        self.speedy= 0
        self.image.set_colorkey(WHITE)

    def update(self):
        self.rect.x += self.speedx
            

class Vida(pg.sprite.Sprite):
    #construtor da classe
    def __init__(self, px, py):
        pg.sprite.Sprite.__init__(self)
        vida_img = pg.image.load(path.join(img_dir, "coracao.png")).convert()
        self.image = vida_img
        self.image = pg.transform.scale(vida_img, (40, 32))
        self.rect=self.image.get_rect()
        self.rect.x=px
        self.rect.y=py
        self.speedx= -velocidade
        self.speedy= 0
        self.image.set_colorkey(BLACK)

    def update(self):
        self.rect.x += self.speedx
        
class Aguia(pg.sprite.Sprite):
    #construtor da classe
    def __init__(self, px, py):
        pg.sprite.Sprite.__init__(self)
        aguia_img = pg.image.load(path.join(img_dir, "aguia.png")).convert()
        self.image = aguia_img
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(aguia_img, (40, 30))
        self.rect=self.image.get_rect()
        self.rect.x=px
        self.rect.y=py
        self.speedx= -velocidade
        self.speedy= 0
        
    def update(self):
        
        self.rect.x += self.speedx
        
screen = pg.display.set_mode((WIDTH, HEIGHT))
img_dir = path.join(path.dirname(__file__), 'img')
pg.display.set_caption("Dino Run")
clock = pg.time.Clock()

background = pg.image.load(path.join(img_dir, 'starfield.png')).convert()
TI = pg.image.load(path.join(img_dir, 'telainicial.png')).convert()           
TF = pg.image.load(path.join(img_dir, 'telafinal.png')).convert()  
score_font = pg.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)

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

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Dino Run")
clock = pg.time.Clock()

def tela_inicial():
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

def tela_play():
    player.vida = 3
    cont_Mob = 0
    intervalo_Mob = random.randint(FPS//2, 3*FPS)
    cont_aguia=0
    intervalo_aguia = random.randint(FPS//2, 3*FPS)
    cont_life=0
    prob_vida = random.randint(FPS//2, 3*FPS) 
    cont = 0

    running = True
    score = 0
    
    while running:
        clock.tick(FPS)
          
        if cont_Mob == intervalo_Mob:
            mob = Mob(WIDTH, 260)
            all_sprites.add(mob)
            all_mobs.add(mob)
            cont_Mob = 0
            intervalo_Mob = random.randint(50, 100)

        if cont_aguia == intervalo_aguia:
            aguia = Aguia(WIDTH, 235)
            aguia.speedx -= velocidade
            all_sprites.add(aguia)
            all_aguias.add(aguia)
            cont_aguia = 0
            intervalo_aguia = random.randint(500, 1000)            
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                
            if event.type == pg.KEYDOWN:
                
                if event.key == pg.K_SPACE:
                    
                    if not player.pulando:
                        
                        player.pulando = True
                        player.speedy = -11        
                    
        all_sprites.update()
        screen.fill(BLACK)
                
        hits = pg.sprite.groupcollide(all_players, all_vida,False, True)
        if hits:
           player.vida+=1
        
        hits = pg.sprite.groupcollide(all_players, all_mobs,False, True)
        if not hits:
            
            score += 1
        if hits:
            
           player.vida-=1
        hits = pg.sprite.groupcollide(all_players, all_aguias,False, True)
        if hits:
            
           player.vida-=1

        cont_Mob += 1
        cont_aguia+=1
        cont_life+=1
               
        background_rect1.x -= velocidade             
        background_rect2.x -= velocidade
        screen.blit(background, background_rect1)
        screen.blit(background, background_rect2)
        
        if background_rect1.x<0:
            background_rect1.x = WIDTH
            background_rect2.x = 0
        
        if cont_life == prob_vida:
            vida = Vida(WIDTH, 260)
            all_sprites.add(vida)
            all_vida.add(vida)
            cont_life = 0
            prob_vida = random.randint(60,1000)
            
        if (cont % 8) == 0:
            player.img_index = (player.img_index + 1) % 2 
        cont += 1
        all_sprites.draw(screen)

        text_surface = score_font.render("{:d}".format(player.vida), True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        screen.blit(text_surface, text_rect)
        
        text_surface = score_font.render("{:08d}".format(score), True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        screen.blit(text_surface, text_rect)         
        pg.display.flip()
        
        if score>= 500: 
            aguia.speedx = -5
            mob.speedx = -4
            all_vida.speedx = -4
            
        if score>= 1000: 
            aguia.speedx = -6
            mob.speedx = -5
            all_vida.speedx=-5
            
        if score>= 1500: 
            aguia.speedx = -7
            mob.speedx = -6
            all_vida.speedx=-6
        if score>= 2000: 
            aguia.speedx = -8
            mob.speedx = -7
            all_vida.speedx=-7

        if score>= 2500: 
            aguia.speedx = -9
            mob.speedx = -8
            all_vida.speedx= -8

        if score>= 3000: 
            aguia.speedx = -10
            mob.speedx = -9
            all_vida.speedx=-9

        if score>= 3500: 
            aguia.speedx = -11
            mob.speedx = -10
            all_vida.speedx=-10

        if score>= 4000: 
            aguia.speedx = -12
            mob.speedx = -11
            all_vida.speedx= -11
    
        if player.vida == 0:
            running = False

def tela_final():
    running = True
    while running:
        
        clock.tick(FPS)
        screen.blit(TF, TF.get_rect())
        pg.display.flip()
        for event in pg.event.get():
            
            if event.type == pg.KEYDOWN:
                
                if event.key == pg.K_SPACE:

                    running = False


                    running = False 

                    return True
                if event.key == pg.QUIT:
                    return False
                
try: 
    running = True
    while running:

        tela_inicial()
        tela_play()
        
        running = tela_final()
finally:
    pg.quit()