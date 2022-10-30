import pandas as pd
import matplotlib.pyplot as plt


def read_csv(filename):
    data = pd.read_csv(filename)
    return data


def graph(data):
    pclasses = {}

    for index, row in data.iterrows():
        pclass = row.Pclass
        pclasses[pclass] = pclasses.get(pclass, 0) + 1

    values = list(pclasses.values())
    titles = list(pclasses.keys())
    plt.pie(values, labels=titles, autopct='%.1f%%')
    plt.title('Распредение по количеству класса пассажира')
    plt.show()


if __name__ == '__main__':
    dataset = read_csv("tested.csv")
    graph(dataset)
