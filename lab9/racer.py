import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS \\ частота обновления экрана 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors RGB
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

#Setting up Fonts \\ размер шрифтов и отображения текста на экране 
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
point=pygame.font.SysFont("Verdana", 20)
#изображение фона 
background = pygame.image.load("Street.png")

#Create a white screen \ задается игровое окно заданных размеров и устанавливается заголовок окна 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#класс для Enemy который является подклассом pygame.sprite.Sprite. 
#Враги будут падать сверху экрана, и их позиция будет обновляться 
#с увеличением скорости игры. Когда враг достигает нижней части экрана,
# счет увеличивается на 1.
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#класс определяет самого игрока и он может двигаться вправо и влево с помощью клавиш
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
#класс определяяющий монеты,они падают сверху
#и их позиция обновляется с увеличением скорости игры,
#затем она достигает нижней части и перемещается в случайное место наверху экрана
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Coin.png")
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)
    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top>600):
            self.rect.top=0
            self.rect.center=(random.randint(40, SCREEN_WIDTH-40),0)
                  
#Setting up Sprites \ создаются экземпляры
P1 = Player()
E1 = Enemy()
C1=Coin()
#Creating Sprites Groups \ спрайты-графические объекты
enemies = pygame.sprite.Group()
enemies.add(E1)
coins=pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding a new User event \ для увеличения скорости игры и таймера на 1000мс
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
collected=0
#Game Loop\ бесконечный цикл игры 
while True:
      
    #Cycles through all events occurring 
    #обрабатывает все события в pygame
    for event in pygame.event.get():
        # при увеличения скорости,увеличиваем на 0,5
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
# отображается фон 
    DISPLAYSURF.blit(background, (0,0))
    #отображается счет игрока и все собранные монеты
    scores = font_small.render(str(SCORE), True, BLACK)
    coin_point=point.render(str(collected), True, BLUE)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coin_point,(10,30))
    #Moves and Re-draws all Sprites\ отображение и обновление граф об
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    #To be run if collision occurs between Player and Enemy\ проверка столкновения
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav.mp3').play()
          # 0.5 c перед следующими действиями
          time.sleep(0.5)
        #окно красного цвета для создания эффекта конца игры
          DISPLAYSURF.fill(RED)
          # конец игры
          DISPLAYSURF.blit(game_over, (30,250))
          # обновление окна игры и  отображение предыдущих действии
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
                # пауза на 2 с перед закрытием игры
          time.sleep(2)
          # завершение программы и закрытие приложения
          pygame.quit()
          sys.exit()   

    # столкновение с монетой
    if pygame.sprite.spritecollideany(P1, coins):
        collected+=10
        C1.rect.center=(random.randint(40, SCREEN_WIDTH-40),0)
        SPEED+=0.5

        
    pygame.display.update()
    FramePerSec.tick(FPS) 