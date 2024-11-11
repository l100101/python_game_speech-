import pygame
import random

# Инициализация pygame
pygame.init()

# Создание окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Название игры
pygame.display.set_caption("Пересечение объектов")

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Массивы объектов
objects1 = []
objects2 = []

image_A = pygame.image.load("alphabet/A.png")
image_O = pygame.image.load("alphabet/O.png")

# Создание объектов
for i in range(10):
    # objects1.append(pygame.Rect(50 + i * 70, 50, 50, 50))
    objects1.append(pygame.Rect(50 + i * 70, 50, image_A.get_width(), image_A.get_height()))
    objects2.append(pygame.Rect(50 + i * 70, 300, 50, 50))

# Переменная для хранения перетаскиваемого объекта
dragging = None

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for obj in objects2:
                if obj.collidepoint(event.pos):
                    dragging = obj
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = None
        elif event.type == pygame.MOUSEMOTION and dragging:
            dragging.x = event.pos[0] - dragging.width // 2
            dragging.y = event.pos[1] - dragging.height // 2

    # Очистка экрана
    screen.fill(white)

    # Рисование объектов
    for obj in objects1:
        screen.blit(image_A, obj)
        # screen.blit(image_O, obj)
    for obj in objects2:
        pygame.draw.rect(screen, blue, obj, 5)

    # Проверка пересечения объектов
    for obj1 in objects1:
        for obj2 in objects2:
            if obj1.colliderect(obj2):
                print("Пересечение!")

    # Обновление экрана
    pygame.display.flip()

    # Ограничение скорости игры
    pygame.time.Clock().tick(60)