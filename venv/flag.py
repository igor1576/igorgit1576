import pygame

pygame.init()

# Считываем размер окна
size = width, height = 300, 300
screen = pygame.display.set_mode(size)


def draw():
    # Задаем параметры прямоугольника
    rect_color = pygame.Color('white')
    rect_width = 0
    rect_point = [(0, 0), (300, 100)]
    # Рисуем прямоугольник
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)

    rect_color = pygame.Color('blue')
    rect_width = 0
    rect_point = [(0, 100), (300, 100)]
    # Рисуем прямоугольник
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)

    rect_color_red = pygame.Color('red')
    rect_width_red = 0
    rect_point_red = [(0, 200), (300, 100)]
    # Рисуем прямоугольник
    pygame.draw.rect(screen, rect_color_red, rect_point_red, rect_width_red

    rect_color = pygame.Color('black')
    rect_width = 0
    rect_point = [(0, 0), (10, 300)]
    # Рисуем прямоугольник
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
