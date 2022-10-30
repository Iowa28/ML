import math

import pandas as pd
import matplotlib.pyplot as plt


def read_csv(filename):
    data = pd.read_csv(filename)
    return data


def graph(data):
    genders = data.gender
    print(len(genders))
    ages = list(data['age'])
    colors = []
    for i in range(len(genders)):
        if genders[i] == 'm':
            colors.append('b')
        else:
            colors.append('r')
    plt.bar(range(genders), ages, color=colors)
    plt.plot()


if __name__ == '__main__':
    # n = 100
    # print(int(math.sqrt(n)))
    abc = [i for i in range(1, 11)]
    print(abc)