import pygame
pygame.init()

# Окно игры
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Draw circle")

# Цвета
ball_color = pygame.Color('blue')
bg_color = pygame.Color('white')

# Параметры шара
ball_pos = [400, 300]
ball_radius = 25
speed = 20

# Ограничение FPS
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ball_pos[1] = max(ball_pos[1] - speed, 0)  # Верхняя граница
    if keys[pygame.K_s]:
        ball_pos[1] = min(ball_pos[1] + speed, window_size[1] - ball_radius * 2)  # Нижняя граница
    if keys[pygame.K_a]:
        ball_pos[0] = max(ball_pos[0] - speed, 0)  # Левая граница
    if keys[pygame.K_d]:
        ball_pos[0] = min(ball_pos[0] + speed, window_size[0] - ball_radius * 2)  # Правая граница

    # Отрисовка
    screen.fill(bg_color)
    pygame.draw.circle(screen, ball_color, (ball_pos[0] + ball_radius, ball_pos[1] + ball_radius), ball_radius)
    pygame.display.flip()
    
    clock.tick(24)  # Ограничение FPS

pygame.quit()