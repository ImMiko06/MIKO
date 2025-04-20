import pygame

# Инициализация параметров окна
WIDTH, HEIGHT = 1200, 800  # Определяет ширину и высоту окна игры
FPS = 90  # Частота обновления экрана (кадры в секунду)
draw = False  # Переменная, указывающая рисуем ли на экране
radius = 2  # Радиус кисти
color = 'blue'  # Цвет кисти
mode = 'pen'  # Режим рисования (по умолчанию кисть)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Создание окна с заданными размерами
pygame.display.set_caption('Paint')  # Название окна
clock = pygame.time.Clock()  # Для управления временем (контроль FPS)
screen.fill(pygame.Color('white'))  # Заполнение экрана белым цветом
font = pygame.font.SysFont('None', 60)  # Создание шрифта для отображения текста

# Функция для рисования линии
def drawLine(screen, start, end, width, color):
    # Извлечение координат x и y начальной и конечной точек
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    
    # Вычисление абсолютных разниц между x и y координатами
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    # Коэффициенты для уравнения прямой Ax + By + C = 0
    A = y2 - y1  # Вертикальный коэффициент
    B = x1 - x2  # Горизонтальный коэффициент
    C = x2 * y1 - x1 * y2 
    
    # Если линия более горизонтальная, чем вертикальная
    if dx > dy:
        # Убедимся, что x1 слева от x2
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        # Итерация по координатам x
        for x in range(x1, x2):
            # Вычисление y координаты с использованием уравнения прямой
            y = (-C - A * x) / B
            # Рисуем пиксель (круг) в позиции (x, y)
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)
    # Если линия более вертикальная, чем горизонтальная
    else:
        # Убедимся, что y1 ниже y2
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        # Итерация по координатам y
        for y in range(y1, y2):
            # Вычисление x координаты с использованием уравнения прямой
            x = (-C - B * y) / A
            # Рисуем пиксель (круг) в позиции (x, y)
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)

# Функция для рисования круга
def drawCircle(screen, start, end, width, color):
    # Извлечение координат x и y начальной и конечной точек
    x1 = start[0]  # Извлекаем x координату начальной точки
    x2 = end[0]  # Извлекаем x координату конечной точки
    y1 = start[1]  # Извлекаем y координату начальной точки
    y2 = end[1]  # Извлекаем y координату конечной точки
    
    # Вычисление центра круга
    x = (x1 + x2) / 2  # Вычисляем центр круга по оси x
    y = (y1 + y2) / 2  # Вычисляем центр круга по оси y
    
    # Вычисление радиуса круга
    radius = abs(x1 - x2) / 2  # Вычисляем радиус круга
    
    # Рисуем круг на экране
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)  # Рисуем круг на экране

# Функция для рисования прямоугольника
def drawRectangle(screen, start, end, width, color):
    # Извлечение координат x и y начальной и конечной точек
    x1 = start[0]  # Извлекаем x координату начальной точки
    x2 = end[0]  # Извлекаем x координату конечной точки
    y1 = start[1]  # Извлекаем y координату начальной точки
    y2 = end[1]  # Извлекаем y координату конечной точки
    
    # Вычисление ширины и высоты прямоугольника
    widthr = abs(x1 - x2)  # Ширина прямоугольника
    height = abs(y1 - y2)  # Высота прямоугольника
    
    # Рисуем прямоугольник на экране, исходя из начальной и конечной точек
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)  # Рисуем прямоугольник на экране
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)  # Рисуем прямоугольник на экране
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)  # Рисуем прямоугольник на экране
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)  # Рисуем прямоугольник на экране

# Функция для рисования квадрата
def drawSquare(screen, start, end, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    mn = min(abs(x2 - x1), abs(y2 - y1))  # Вычисляем минимальное расстояние для стороны квадрата
    
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
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    
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
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    
    # Ширина основания треугольника
    width_b = abs(x2 - x1)
    height = (3**0.5) * width_b / 2  # Высота равностороннего треугольника
    
    # Рисуем равносторонний треугольник
    if y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), width)
    else:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)))

# Функция для рисования ромба
def drawRhombus(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    
    # Рисуем ромб
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
