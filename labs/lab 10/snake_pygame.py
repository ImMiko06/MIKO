import pygame
import random
import psycopg2
import sys

# === Ввод имени ===
username = input("Введите имя игрока (до 50 символов): ")
if len(username) > 50:
    print("❌ Имя слишком длинное!")
    sys.exit()

# === Подключение к базе PostgreSQL ===
try:
    conn = psycopg2.connect(
        host="localhost",
        dbname="lab 10", 
        user="postgres",
        password="140506",
        port=5432
    )
    cur = conn.cursor()
except Exception as e:
    print("❌ Ошибка подключения к базе:", e)
    sys.exit()

def get_user(username):
    cur.execute("SELECT id FROM game_user WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
        print(f"👤 Игрок найден. Начинаем новую игру.")
        return user_id, 1, 0
    else:
        cur.execute("INSERT INTO game_user (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        print("🆕 Новый игрок создан.")
        return user_id, 1, 0

def save_score(user_id, level, score):
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
    conn.commit()
    print("✅ Результат сохранён.")

# === Инициализация Pygame ===
pygame.init()
WIDTH, HEIGHT = 600, 400
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake with Full Border Walls")
clock = pygame.time.Clock()

# === Цвета ===
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
GRAY = (100, 100, 100)

# === Загрузка изображений ===
bg_img = pygame.image.load(r"C:\All Labka\labs\lab 10\background.jpg")
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
apple_img = pygame.image.load(r"C:\All Labka\labs\lab 10\apple.png")
apple_img = pygame.transform.scale(apple_img, (CELL, CELL))
gold_apple_img = pygame.image.load(r"C:\All Labka\labs\lab 10\gold_apple.png")
gold_apple_img = pygame.transform.scale(gold_apple_img, (CELL, CELL))

def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], CELL, CELL))

def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, GRAY, pygame.Rect(wall[0], wall[1], CELL, CELL))

def draw_text(text, x, y, size=30):
    font = pygame.font.SysFont("Arial", size)
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

def draw_food(pos, is_gold):
    img = gold_apple_img if is_gold else apple_img
    screen.blit(img, (pos[0], pos[1]))

# === Генерация полной рамки ===
def generate_walls(level):
    if level == 1:
        return []

    margin = (level - 2) * CELL
    walls = []

    # Горизонтали (верх и низ)
    for x in range(margin, WIDTH - margin, CELL):
        walls.append([x, margin])  # верхняя
        walls.append([x, HEIGHT - CELL - margin])  # нижняя

    # Вертикали (лево и право)
    for y in range(margin, HEIGHT - margin, CELL):
        walls.append([margin, y])  # левая
        walls.append([WIDTH - CELL - margin, y])  # правая

    # Добавим правый нижний угол
    walls.append([WIDTH - CELL - margin, HEIGHT - CELL - margin])

    return walls

# === Позиция еды вне стены и змеи ===
def get_random_food_position(snake, walls):
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if [x, y] not in snake and [x, y] not in walls:
            return [x, y]

# === Главный игровой цикл ===
def game_loop(user_id, level, score):
    snake = [[100, 100]]
    direction = [CELL, 0]
    walls = generate_walls(level)
    food = get_random_food_position(snake, walls)
    gold_counter = 0
    is_gold = False
    speed = 5 + level * 1.25
    running = True
    paused = False

    # Стартовая пауза
    waiting = True
    while waiting:
        screen.blit(bg_img, (0, 0))
        draw_text("Нажмите любую клавишу для старта", WIDTH // 2 - 180, HEIGHT // 2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    while running:
        screen.blit(bg_img, (0, 0))
        draw_snake(snake)
        draw_food(food, is_gold)
        draw_walls(walls)
        draw_text(f"Очки: {score}  Уровень: {level}", 10, 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(user_id, level, score)
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = [-CELL, 0]
                elif event.key == pygame.K_RIGHT:
                    direction = [CELL, 0]
                elif event.key == pygame.K_UP:
                    direction = [0, -CELL]
                elif event.key == pygame.K_DOWN:
                    direction = [0, CELL]
                elif event.key == pygame.K_p:
                    paused = not paused

        if paused:
            draw_text("⏸ Пауза", WIDTH // 2 - 50, HEIGHT // 2)
            pygame.display.flip()
            clock.tick(5)
            continue

        new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

        if (new_head in snake or
            new_head in walls or
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            save_score(user_id, level, score)
            print("💥 Столкновение!")
            running = False

        snake.insert(0, new_head)

        if new_head == food:
            if is_gold:
                score += 30
                level += 1
                speed += 1.25
                walls = generate_walls(level)
            else:
                score += 10
                gold_counter += 1

            is_gold = (gold_counter >= 5)
            if is_gold:
                gold_counter = 0

            food = get_random_food_position(snake, walls)
        else:
            snake.pop()

        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()
    cur.close()
    conn.close()

# === Старт игры ===
if __name__ == "__main__":
    user_id, level, score = get_user(username)
    game_loop(user_id, level, score)
