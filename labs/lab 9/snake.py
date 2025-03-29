import pygame
import sys
import copy
import random
import time

pygame.init()

# Параметры игры
scale = 15
score = 0
level = 0
SPEED = 10
WIDTH = 500
HEIGHT = 500

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Цвета
background_top = (0, 0, 50)
background_bottom = (0, 0, 0)
snake_colour = (255, 137, 0)
snake_head = (255, 247, 0)
font_colour = (255, 255, 255)
defeat_colour = (255, 0, 0)
button_colour = (30, 144, 255)
hover_colour = (70, 160, 255)

# Класс змейки
class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        self.w = scale
        self.h = scale
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def reset(self):
        self.x = WIDTH / 2 - scale
        self.y = HEIGHT / 2 - scale
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def show(self):
        for i in range(self.length):
            color = snake_colour if i != 0 else snake_head
            pygame.draw.rect(display, color, (self.history[i][0], self.history[i][1], self.w, self.h))

    def check_eaten(self, food):
        if abs(self.history[0][0] - food.x) < scale and abs(self.history[0][1] - food.y) < scale:
            return True
        return False

    def check_level(self):
        global level
        if self.length % 5 == 0:
            return True

    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length - 2])

    def death(self):
        if self.length < 4:
            return False
        for i in range(4, self.length):
            if self.history[0] == self.history[i]:
                return True
        return False

    def update(self):
        for i in range(self.length - 1, 0, -1):
            self.history[i] = copy.deepcopy(self.history[i - 1])
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale

# Класс еды
class Food:
    def __init__(self):
        self.new_location()

    def new_location(self):
        self.x = random.randrange(1, int(WIDTH / scale) - 1) * scale
        self.y = random.randrange(1, int(HEIGHT / scale) - 1) * scale
        self.spawn_time = time.time()
        self.value = random.choice([1, 3, 5])
        if self.value == 1:
            self.color = (0, 255, 0)
        elif self.value == 3:
            self.color = (255, 165, 0)
        elif self.value == 5:
            self.color = (255, 0, 0)

    def show(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, scale, scale))

    def is_expired(self):
        return time.time() - self.spawn_time > 5

# Отображение текста на экране
def draw_text(text, size, color, x, y, center=True):
    font = pygame.font.SysFont(None, size)
    rendered = font.render(text, True, color)
    rect = rendered.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    display.blit(rendered, rect)
    return rect

# Кнопка (прямоугольник с текстом)
def draw_button(text, x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    hovered = x < mouse[0] < x + w and y < mouse[1] < y + h
    color = hover_colour if hovered else button_colour
    pygame.draw.rect(display, color, (x, y, w, h), border_radius=10)
    text_rect = draw_text(text, 30, (255, 255, 255), x + w // 2, y + h // 2)
    return hovered and click[0]

# Показать очки и уровень
def show_score():
    draw_text("Score: " + str(score), 20, font_colour, scale, scale, center=False)

def show_level():
    draw_text("Level: " + str(level), 20, font_colour, 90 - scale, scale, center=False)

# Экран меню
def main_menu():
    while True:
        display.fill((10, 10, 30))
        draw_text("SNAKE GAME", 60, font_colour, WIDTH // 2, 150)
        if draw_button("Start Game", WIDTH // 2 - 100, 250, 200, 60):
            break
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Экран Game Over
def game_over_screen():
    while True:
        display.fill((30, 0, 0))
        draw_text("GAME OVER", 60, defeat_colour, WIDTH // 2, 180)
        if draw_button("Restart", WIDTH // 2 - 100, 280, 200, 60):
            return  # возвращаемся в игру
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Основной цикл игры
def game_loop():
    global score, level, SPEED

    snake = Snake(WIDTH / 2, HEIGHT / 2)
    food = Food()
    score = 0
    level = 0
    SPEED = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if snake.y_dir == 0:
                    if event.key == pygame.K_UP:
                        snake.x_dir = 0
                        snake.y_dir = -1
                    if event.key == pygame.K_DOWN:
                        snake.x_dir = 0
                        snake.y_dir = 1
                if snake.x_dir == 0:
                    if event.key == pygame.K_LEFT:
                        snake.x_dir = -1
                        snake.y_dir = 0
                    if event.key == pygame.K_RIGHT:
                        snake.x_dir = 1
                        snake.y_dir = 0

        # Фон
        for y in range(HEIGHT):
            color = (
                background_top[0] + (background_bottom[0] - background_top[0]) * y / HEIGHT,
                background_top[1] + (background_bottom[1] - background_top[1]) * y / HEIGHT,
                background_top[2] + (background_bottom[2] - background_top[2]) * y / HEIGHT
            )
            pygame.draw.line(display, color, (0, y), (WIDTH, y))

        snake.show()
        snake.update()
        food.show()
        show_score()
        show_level()

        if snake.check_eaten(food):
            score += food.value
            snake.grow()
            food = Food()

        if food.is_expired():
            food = Food()

        if snake.check_level():
            level += 1
            SPEED += 1
            snake.grow()

        if snake.death() or snake.history[0][0] < 0 or snake.history[0][0] >= WIDTH or \
           snake.history[0][1] < 0 or snake.history[0][1] >= HEIGHT:
            game_over_screen()
            return  # выйти из цикла и перезапустить

        pygame.display.update()
        clock.tick(SPEED)

# Запуск игры
while True:
    main_menu()
    game_loop()