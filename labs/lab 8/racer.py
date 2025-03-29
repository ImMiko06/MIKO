import pygame, sys
from pygame.locals import *
import random, time

# Инициализация Pygame
pygame.init()

# FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Создание цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Другие переменные для использования в программе
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
SCORE = 0
COINS = 0

# Настройка шрифтов
font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Загрузка фона
background = pygame.image.load(r"C:\\All Labka\\labs\\lab 8\\racer things\\AnimatedStreet.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Масштабируем фон под размер экрана

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Racer")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\\All Labka\\labs\\lab 8\\racer things\\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Добавление класса Coin для появления монет и подсчета их количества
c1, c2, c3, c4, c5 = False, False, False, False, False
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\\All Labka\\labs\\lab 8\\racer things\\coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))

    def move(self):
        global COINS
        global SPEED
        # Добавление различных бонусов в зависимости от положения монеты
        if self.rect.bottom < SCREEN_HEIGHT // 3:
            COINS += 3
        elif self.rect.bottom < SCREEN_HEIGHT // 1.5:
            COINS += 2
        else:
            COINS += 1
        global c1, c2, c3, c4, c5
        if not c1 and COINS >= 10:
            SPEED += 1
            c1 = True
        if not c2 and COINS >= 20:
            SPEED += 1
            c2 = True
        if not c3 and COINS >= 30:
            SPEED += 1
            c3 = True
        if not c4 and COINS >= 40:
            SPEED += 1
            c4 = True
        if not c5 and COINS >= 50:
            SPEED += 1
            c5 = True
        self.rect.top = random.randint(40, SCREEN_WIDTH - 40)
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\\All Labka\\labs\\lab 8\\racer things\\player.png")
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
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)

# Настройка спрайтов
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
coinss = pygame.sprite.Group()
coinss.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Добавление нового пользовательского события
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

def game_over_screen():
    screen.fill(RED)
    screen.blit(game_over, (30, 250))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:  # Продолжить игру при нажатии на пробел
                    return True
                elif event.key == K_ESCAPE:  # Закончить игру при нажатии на ESC
                    return False

def handle_crash():
    time.sleep(2)

background_y = 0  # Инициализация координаты Y для фона

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Если есть столкновение между игроком и врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        continue_game = handle_crash()
        if not continue_game:
            pygame.quit()
            sys.exit()

    # Прокручиваем фон
    background_y = (background_y + SPEED) % background.get_height()

    # Рисуем фон в текущем положении
    screen.blit(background, (0, background_y))  # Отображаем первую часть фона
    screen.blit(background, (0, background_y - background.get_height()))  # Отображаем вторую часть фона для непрерывной прокрутки

    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))

    coins = font_small.render(str(COINS), True, BLACK)
    screen.blit(coins, (370, 10))

    # Двигаем и перерисовываем все спрайты
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

        # Увеличиваем количество монет при столкновении с игроком
        if entity == C1:
            if pygame.sprite.spritecollideany(P1, coinss):
                entity.move()
        else:
            entity.move()

    # Двигаем второй случайный автомобиль
    for enemy in enemies:
        enemy.move()

    # Двигаем монеты
    for coin in coinss:
        coin.rect.y += SPEED

        # Если монета выходит за пределы экрана, респавним её
        if coin.rect.top > SCREEN_HEIGHT:
            coin.rect.y = -coin.rect.height
            coin.rect.x = random.randint(40, SCREEN_WIDTH - 40)

    pygame.display.update()
    FramePerSec.tick(FPS)
