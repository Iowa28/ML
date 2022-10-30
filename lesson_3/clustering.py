import math
import random
import sys
import time

import matplotlib.pyplot as plt
from datetime import datetime


def get_datetime():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S.%f'")[:-3]


def generate_spots(count, resolution):
    random_spots = []

    for i in range(0, count):
        x = random.randint(-resolution, resolution)
        y = random.randint(-resolution, resolution)
        random_spots.append({'x': x, 'y': y})

    return random_spots


def show_spots(spots):
    for spot in spots:
        plt.scatter(spot['x'], spot['y'], color='gray')

    plt.title('Spots ' + get_datetime())
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.grid()
    plt.draw()


def show_clustered_spots(spots, centroids):
    for spot in spots:
        center = spot['center']
        plt.scatter(spot['x'], spot['y'], color=center['color'])

    for centroid in centroids:
        plt.plot(centroid['x'], centroid['y'], '+g')

    plt.title('Spots ' + get_datetime())
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.grid()
    plt.draw()


def show_spots_colorized(spots):
    for spot in spots:
        plt.scatter(spot['x'], spot['y'], color=spot['color'])

    plt.title('Spots' + get_datetime())
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.grid()
    plt.draw()


def calculate_center(spots):
    center = {'x': 0, 'y': 0}

    for spot in spots:
        center['x'] += spot['x']
        center['y'] += spot['y']

    center['x'] /= len(spots)
    center['y'] /= len(spots)
    return center


def calculate_euclidean_metric(spot, center):
    euclidean_metric = math.sqrt((spot['x'] - center['x']) ** 2 + (spot['y'] - center['y']) ** 2)

    return euclidean_metric


def calculate_radius(spots, center):
    radius = 0

    for spot in spots:
        euclidean_metric = calculate_euclidean_metric(spot, center)

        if euclidean_metric > radius:
            radius = euclidean_metric

    return radius


def initial_centroids(k, radius, center):
    x_center = center['x']
    y_center = center['y']
    centroids = []

    for i in range(1, k + 1):
        x = radius * math.cos(2 * math.pi * i / k) + x_center
        y = radius * math.sin(2 * math.pi * i / k) + y_center
        centroids.append({
            'id': i,
            'x': x,
            'y': y
        })

    return centroids


def colorize_centers(centers):
    colorized_centers = []

    color_map = plt.cm.get_cmap('hsv', len(centers) + 1)
    for i, center in enumerate(centers):
        colorized_centers.append({
            'id': center['id'],
            'x': center['x'],
            'y': center['y'],
            'color': color_map(i)
        })

    return colorized_centers


def cluster_spots(spots, centers):
    clustered_spots = []

    for spot in spots:
        nearest_center = None
        nearest_center_distance = sys.maxsize

        for center in centers:
            euclidean_metric = calculate_euclidean_metric(spot, center)

            if euclidean_metric < nearest_center_distance:
                nearest_center = center
                nearest_center_distance = euclidean_metric

        clustered_spots.append({
            'x': spot['x'],
            'y': spot['y'],
            'center': nearest_center
        })

    return clustered_spots


def get_center_spots(center, spots):
    center_spots = []
    for spot in spots:
        spot_center = spot['center']
        if spot_center['id'] == center['id']:
            center_spots.append(spot)

    return center_spots


def compare_centers(center_1, center_2):
    center_1_x = round(center_1['x'])
    center_1_y = round(center_1['y'])
    center_2_x = round(center_2['x'])
    center_2_y = round(center_2['y'])

    return center_1_x == center_2_x and center_1_y == center_2_y


if __name__ == '__main__':
    pause = .1
    resolution = 1000
    spots_number = 100
    spots = generate_spots(spots_number, resolution)

    k = int(math.sqrt(spots_number))
    # k = 4

    initial_center = calculate_center(spots)
    radius = calculate_radius(spots, initial_center)
    centroids = initial_centroids(k, radius, initial_center)
    centroids = colorize_centers(centroids)
    # for centroid in centroids:
    #     print(centroid['id'], centroid['color'])

    show_spots(spots)
    plt.show()
    time.sleep(pause)

    clustered_spots = cluster_spots(spots, centroids)
    show_clustered_spots(clustered_spots, centroids)
    plt.show()
    time.sleep(pause)

    center_changed = True
    while center_changed:
        new_centroids = []
        for centroid in centroids:
            centroid_spots = get_center_spots(centroid, clustered_spots)

            new_center = calculate_center(centroid_spots)
            new_center['id'] = centroid['id']
            new_center['color'] = centroid['color']

            center_changed = not compare_centers(centroid, new_center)

            if center_changed:
                new_centroids.append(new_center)
            else:
                new_centroids.append(centroid)

        if center_changed:
            centroids = new_centroids

            clustered_spots = cluster_spots(spots, centroids)
            show_clustered_spots(clustered_spots, centroids)
            plt.show()
            time.sleep(pause)
