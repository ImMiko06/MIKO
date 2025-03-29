import pygame
import os

# Инициализация Pygame и микшера
pygame.init()
pygame.mixer.init()

# Пути к изображениям и музыке
song_elements_path = r"C:\\All Labka\\labs\\lab 7\\song elements"

# Загрузка кнопок
playb = pygame.image.load(os.path.join(song_elements_path, "play.png"))
pausb = pygame.image.load(os.path.join(song_elements_path, "pause.png"))
nextb = pygame.image.load(os.path.join(song_elements_path, "next.png"))
prevb = pygame.image.load(os.path.join(song_elements_path, "back.png"))

# Пути к музыкальным файлам
music_files = [
    os.path.join(song_elements_path, "song1.mp3"),
    os.path.join(song_elements_path, "song2.mp3"),
    os.path.join(song_elements_path, "song3.mp3")
]

# Пути к фоновым изображениям для каждой песни
background_images = [
    os.path.join(song_elements_path, "background1.png"),
    os.path.join(song_elements_path, "background2.png"),
    os.path.join(song_elements_path, "background3.png")
]

# Загрузка начального фона
current_song = 0
background = pygame.image.load(background_images[current_song])

# Загрузка кнопок и изменение их размера
playb = pygame.transform.scale(playb, (50, 50))
pausb = pygame.transform.scale(pausb, (50, 50))
nextb = pygame.transform.scale(nextb, (50, 50))
prevb = pygame.transform.scale(prevb, (50, 50))
background = pygame.transform.scale(background, (800, 600))

# Инициализация музыки
pygame.mixer.music.load(music_files[current_song])

# Окно
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# Координаты кнопок
play_rect = pygame.Rect(300, 400, 50, 50)
pause_rect = pygame.Rect(400, 400, 50, 50)
next_rect = pygame.Rect(500, 400, 50, 50)
prev_rect = pygame.Rect(200, 400, 50, 50)

running = True
while running:
    screen.blit(background, (0, 0))  # Отображение текущего фона
    screen.blit(playb, play_rect.topleft)
    screen.blit(pausb, pause_rect.topleft)
    screen.blit(nextb, next_rect.topleft)
    screen.blit(prevb, prev_rect.topleft)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                pygame.mixer.music.play()
            elif pause_rect.collidepoint(event.pos):
                pygame.mixer.music.pause()
            elif next_rect.collidepoint(event.pos):
                # Переключение на следующую песню
                current_song = (current_song + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_song])
                pygame.mixer.music.play()
                
                # Загрузка нового фона для текущей песни
                background = pygame.image.load(background_images[current_song])
                background = pygame.transform.scale(background, (800, 600))
            elif prev_rect.collidepoint(event.pos):
                # Переключение на предыдущую песню
                current_song = (current_song - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_song])
                pygame.mixer.music.play()
                
                # Загрузка нового фона для текущей песни
                background = pygame.image.load(background_images[current_song])
                background = pygame.transform.scale(background, (800, 600))
    
    pygame.display.flip()

pygame.quit()
