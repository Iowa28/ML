import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


def dist(point_a, point_b):
    return np.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)


def random_points(n):
    points = make_blobs(n)
    return points[0]


def draw(points):
    plt.scatter(points[,0:], points[:,0])
    plt.show()


def calculate_mean(points, cluster_number = 0):
    x_mean = 0
    y_mean = 0
    quantity = 0

    for i in range(len(points)):
        x_mean += points[i][0]
        y_mean += points[i][1]
        quantity += 1
    x_mean /= quantity
    y_mean /= quantity

    return [x_mean, y_mean]


def init_centers(points, k):
    x_m, y_m = calculate_mean()[0], calculate_mean()[1]


if __name__ == '__main__':
    n = 100
    points = random_points(n)
