import pygame

# Инициализация параметров окна
WIDTH, HEIGHT = 1200, 800  # Ширина и высота окна игры
FPS = 90  # Частота обновления экрана (кадры в секунду)
draw = False  # Переменная для указания, рисуем ли мы
radius = 2  # Радиус кисти
color = 'blue'  # Цвет кисти
mode = 'pen'  # Режим рисования (по умолчанию — кисть)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Создание окна с заданными размерами
pygame.display.set_caption('Paint')  # Название окна
clock = pygame.time.Clock()  # Для управления временем (контроль FPS)
screen.fill(pygame.Color('white'))  # Заполнение экрана белым цветом
font = pygame.font.SysFont('None', 60)  # Создание шрифта для отображения текста

# Функция для рисования линии
def drawLine(screen, start, end, width, color):
    x1, y1 = start  # Начальная точка
    x2, y2 = end  # Конечная точка

    # Вычисляем абсолютные разницы по осям x и y
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    # Коэффициенты для уравнения линии (Ax + By + C = 0)
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    # Если линия горизонтальная или близка к горизонтальной
    if dx > dy:
        # Убедимся, что x1 всегда меньше x2
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        # Рисуем линии по координатам x
        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)
    else:  # Если линия вертикальная или близка к вертикальной
        # Убедимся, что y1 всегда меньше y2
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        # Рисуем линии по координатам y
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)

# Функция для рисования круга
def drawCircle(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end

    # Находим центр круга
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2

    # Радиус круга
    radius = abs(x1 - x2) / 2

    # Рисуем круг
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)

# Функция для рисования прямоугольника
def drawRectangle(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end

    # Вычисляем ширину и высоту прямоугольника
    widthr = abs(x1 - x2)
    height = abs(y1 - y2)

    # Рисуем прямоугольник в зависимости от положения точек
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)

# Функция для рисования квадрата
def drawSquare(screen, start, end, color):
    x1, y1 = start
    x2, y2 = end
    mn = min(abs(x2 - x1), abs(y2 - y1))

    # Рисуем квадрат в зависимости от положения точек
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, mn, mn))
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, mn, mn))
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, mn, mn))
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn))

# Функция для рисования прямоугольного треугольника
def drawRightTriangle(screen, start, end, color):
    x1, y1 = start
    x2, y2 = end

    # Рисуем прямоугольный треугольник
    if x2 > x1 and y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
    if y2 > y1 and x1 > x2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
    if x1 > x2 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1)))
    if x2 > x1 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1)))

# Функция для рисования равностороннего треугольника
def drawEquilateralTriangle(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end

    # Ширина основания треугольника
    width_b = abs(x2 - x1)
    height = (3 ** 0.5) * width_b / 2

    # Рисуем равносторонний треугольник
    if y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), width)
    else:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)))

# Функция для рисования ромба
def drawRhombus(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2),
                                                           ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), width)

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()  # Закрытие программы при закрытии окна

        # Обработка событий с клавишами
        if event.type == pygame.KEYDOWN:
            # Изменяем режим рисования в зависимости от нажатой клавиши
            if event.key == pygame.K_r:
                mode = 'rectangle'  # Режим прямоугольника
            if event.key == pygame.K_c:
                mode = 'circle'  # Режим круга
            if event.key == pygame.K_p:
                mode = 'pen'  # Режим кисти
            if event.key == pygame.K_e:
                mode = 'erase'  # Режим стирания
            if event.key == pygame.K_s:
                mode = 'square'  # Режим квадрата
            if event.key == pygame.K_q:
                screen.fill(pygame.Color('white'))  # Очистить экран белым цветом

            # Изменение цвета в зависимости от нажатой клавиши
            if event.key == pygame.K_1:
                color = 'black'  # Черный цвет
            if event.key == pygame.K_2:
                color = 'green'  # Зеленый цвет
            if event.key == pygame.K_3:
                color = 'red'  # Красный цвет
            if event.key == pygame.K_4:
                color = 'blue'  # Синий цвет
            if event.key == pygame.K_5:
                color = 'yellow'  # Желтый цвет
            if event.key == pygame.K_t:
                mode = 'right_tri'  # Режим прямоугольного треугольника
            if event.key == pygame.K_u:
                mode = 'eq_tri'  # Режим равностороннего треугольника
            if event.key == pygame.K_h:
                mode = 'rhombus'  # Режим ромба

        # Обработка нажатия кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True  # Включаем рисование
            if mode == 'pen':
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)  # Рисуем точку, если активен режим кисти
            prevPos = event.pos  # Сохраняем начальную позицию мыши

        # Обработка отпускания кнопки мыши
        if event.type == pygame.MOUSEBUTTONUP:
            if mode == 'rectangle':
                drawRectangle(screen, prevPos, event.pos, radius, color)  # Рисуем прямоугольник
            elif mode == 'circle':
                drawCircle(screen, prevPos, event.pos, radius, color)  # Рисуем круг
            elif mode == 'square':
                drawSquare(screen, prevPos, event.pos, color)  # Рисуем квадрат
            elif mode == 'right_tri':
                drawRightTriangle(screen, prevPos, event.pos, color)  # Рисуем прямоугольный треугольник
            elif mode == 'eq_tri':
                drawEquilateralTriangle(screen, prevPos, event.pos, radius, color)  # Рисуем равносторонний треугольник
            elif mode == 'rhombus':
                drawRhombus(screen, prevPos, event.pos, radius, color)  # Рисуем ромб
            draw = False  # Отключаем рисование

        # Обработка движения мыши
        if event.type == pygame.MOUSEMOTION:
            if draw and mode == 'pen':
                drawLine(screen, lastPos, event.pos, radius, color)  # Рисуем линию, если активен режим кисти
            elif draw and mode == 'erase':
                drawLine(screen, lastPos, event.pos, radius, 'white')  # Стираем линию, если активен режим стирания
            lastPos = event.pos  # Обновляем последнюю позицию мыши

    # Отображение информации о радиусе
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))  # Рисуем белый прямоугольник
    renderRadius = font.render(str(radius), True, pygame.Color(color))  # Отображаем текущий радиус
    screen.blit(renderRadius, (5, 5))  # Отображаем текст на экране

    pygame.display.flip()  # Обновляем экран
    clock.tick(FPS)  # Контролируем частоту обновлений
