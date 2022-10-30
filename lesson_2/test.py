import pandas as pd
import matplotlib.pyplot as plt


def read_csv(filename):
    data = pd.read_csv(filename)
    return data


def plot(dataset):
    date = list(dataset.Date)
    sunspots = list(dataset['Monthly Mean Total Sunspot Number'])

    plt.figure(figsize=(60, 10))
    plt.scatter(date, sunspots)
    plt.plot(date, sunspots)

    # n = 25
    # result = pd.DataFrame(sunspots)
    # rolling_mean = result.rolling(window=n).mean()
    # plt.plot(date, rolling_mean, color='r')

    alpha = .5
    result = [sunspots[0]]
    for i in range(1, len(sunspots)):
        result.append(alpha * sunspots[i] + (1 - alpha) * result[i - 1])
    plt.plot(date, result, color='r')

    plt.show()


if __name__ == '__main__':
    dataset = read_csv("Sunspots.csv")
    plot(dataset)
