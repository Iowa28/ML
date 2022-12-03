import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm


def generate_support_points(count, x_limit, y_limit):
    points = []
    classes = []
    for i in range(count):
        x = np.random.randint(0, x_limit)
        y = np.random.randint(0, y_limit)
        c = np.random.randint(0, 2)
        points.append([x, y])
        classes.append(c)
    return points, classes


def draw_points(points, classes, clf, limit, h):
    for i in range(len(points)):
        point = points[i]
        color = 'r'
        if classes[i] == 0:
            color = 'b'
        plt.scatter(point[0], point[1], color = color)

    xx, yy = np.meshgrid(np.arange(0, limit, h),
                         np.arange(0, limit, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.5)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.suptitle('Метод опорных векторов')
    plt.title('r - класс 1, b - класс 0')
    plt.show()


def run():
    count = 5
    limit = 100
    h = .02

    support_points_result = generate_support_points(count, limit, limit)
    support_points = support_points_result[0]
    points_classes = support_points_result[1]
    print(support_points)
    print(points_classes)

    clf = svm.LinearSVC(dual = True, max_iter = 7600)
    clf.fit(support_points, points_classes)

    draw_points(support_points, points_classes, clf, limit, h)

    new_points = generate_support_points(3, limit, limit)[0]
    for i in range(0, len(new_points)):
        point = new_points[i]
        plt.scatter(point[0], point[1], color = 'g')
    draw_points(support_points, points_classes, clf, limit, h)

    new_point_classes = clf.predict(new_points)
    for i in range(0, len(new_points)):
        point = new_points[i]
        color = 'r'
        if new_point_classes[i] == 0:
            color = 'b'
        plt.scatter(point[0], point[1], color = color)
    draw_points(support_points, points_classes, clf, limit, h)


if __name__ == '__main__':
    run()

