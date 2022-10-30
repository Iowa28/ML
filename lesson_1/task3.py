import pandas as pd
import matplotlib.pyplot as plt


def read_csv(filename):
    data = pd.read_csv(filename)
    return data


def graph(data):
    ages = list(data.Age)
    numbers = [i + 1 for i in range(len(ages))]

    plt.bar(numbers, ages)
    plt.title('Распределение по возрасту')
    plt.ylabel('Возраст')
    plt.xlabel('Номер')
    plt.show()


if __name__ == '__main__':
    dataset = read_csv("tested.csv")
    graph(dataset)