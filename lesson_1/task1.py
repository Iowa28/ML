import pandas as pd
import matplotlib.pyplot as plt


def read_csv(filename):
    data = pd.read_csv(filename)
    return data


def graph(data):
    genders = data.Sex
    pclasses = data.Pclass
    survived = data.Survived
    numbers = []
    colors = []
    tickets = []
    number_index = 1

    for i, pclass in enumerate(pclasses):
        if survived[i] == 1:
            numbers.append(number_index)
            number_index += 1
            tickets.append(pclass)
            #colors.append('b' if genders[i] == 'm' else 'r')
            if genders[i] == 'm':
                colors.append('m')

    plt.bar(numbers, tickets, color=colors)
    plt.title('Распредение по классу билета среди выживших')
    plt.ylabel('Класс билета')
    plt.xlabel('Номер')
    plt.show()


if __name__ == '__main__':
    dataset = read_csv("tested.csv")
    graph(dataset)
