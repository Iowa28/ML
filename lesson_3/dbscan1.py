import pygame
import numpy as np


RADIUS = 7
CIRCLES_DISTANCE = 50


def calculate_distance(point_a, point_b):
    return np.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)


def give_flags(points):
    min_points = 3
    flags = ['' for _ in range(len(points))]
    for i, point in enumerate(points):
        near_points_count = 0
        for j in range(len(points)):
            if i != j and calculate_distance(point, points[j]) < CIRCLES_DISTANCE:
                near_points_count += 1
        if near_points_count >= min_points:
            flags[i] = 'green'

    for i, point in enumerate(points):
        if flags[i] != 'green':
            for j, pnt in enumerate(points):
                if flags[j] == 'green' and calculate_distance(point, pnt) < CIRCLES_DISTANCE:
                    flags[i] = 'yellow'
                    break

    for i in range(len(points)):
        if flags[i] == '':
            flags[i] = 'red'

    return flags


def random_points(point):
    k = 6
    area_radius = 35
    new_points = []
    for i in range(k):
        x = np.random.randint(point[0] - area_radius, point[0] + area_radius)
        y = np.random.randint(point[1] - area_radius, point[1] + area_radius)
        new_points.append([x, y])
    return new_points


def draw():
    points = []
    pygame.init()
    screen = pygame.display.set_mode([800, 600])
    screen.fill(color = 'white')
    pygame.display.update()
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pygame.draw.circle(screen, color = 'black', center = event.pos, radius = RADIUS)
                pygame.display.update()
                points.append(list(event.pos))
                new_points = random_points(points[-1])
                for i in range(len(new_points)):
                    points.append(new_points[i])
                    pygame.draw.circle(screen, color='black', center=new_points[i], radius=RADIUS)
                    pygame.display.update()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                screen.fill(color='white')
                pygame.display.update()

                flags = give_flags(points)
                for i, point in enumerate(points):
                    pygame.draw.circle(screen, color=flags[i], center=point, radius=RADIUS)

                pygame.display.update()


if __name__ == '__main__':
    draw()