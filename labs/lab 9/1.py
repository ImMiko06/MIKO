import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw Triangle with Mouse")

background_color = (255, 255, 255)
triangle_color = (0, 255, 0)
draw = False
start_pos = None

def draw_triangle(surface, start, end, color):
    x1, y1 = start
    x2, y2 = end
    point1 = (x1, y1)
    point2 = (x2, y1)
    point3 = ((x1 + x2) // 2, y2)
    pygame.draw.polygon(surface, color, [point1, point2, point3])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            draw = True

        if event.type == pygame.MOUSEMOTION:
            if draw:
                display.fill(background_color)
                draw_triangle(display, start_pos, event.pos, triangle_color)

        if event.type == pygame.MOUSEBUTTONUP:
            if draw:
                draw_triangle(display, start_pos, event.pos, triangle_color)
                draw = False

    pygame.display.flip()

pygame.quit()
