import pandas as pd
import numpy as np
import operator
import matplotlib.pyplot as plt


def read_data():
    return pd.read_csv('Iris.csv')


def divide_dataset(data):
    indices = np.random.permutation(data.shape[0])
    div = int(0.75 * len(indices))
    development_id, test_id = indices[:div], indices[div:]

    development_set, test_set = data.loc[development_id, :], data.loc[test_id, :]
    return [development_set, test_set]


def euclidean_distance(data_1, data_2, data_len, data_mean, data_std):
    n_dist = 0
    for i in range(1, data_len):
        n_dist += np.square(
            (data_1[i] - data_mean[i]) / data_std[i] - (data_2[i] - data_mean[i]) / data_std[i]
        )
    return np.sqrt(n_dist)


def knn(dataset, dev_set, testInstance, k, dataset_mean, dataset_std):
    distances = {}
    # length = testInstance.shape[1]
    length = len(testInstance)

    for index, row in dev_set.iterrows():
        dist_up = euclidean_distance(testInstance, row, length, dataset_mean, dataset_std)
        distances[index + 1] = dist_up

    sort_distances = sorted(distances.items(), key=operator.itemgetter(1))
    neighbors = []

    for x in range(1, k + 1):
        neighbors.append(sort_distances[x - 1][0])

    counts = {"Iris-setosa": 0, "Iris-versicolor": 0, "Iris-virginica": 0}

    for x in range(len(neighbors)):
        neighbor = neighbors[x]
        species = dataset.iloc[neighbor - 1][-1]
        if species in counts:
            counts[species] += 1
        else:
            counts[species] = 1

    sort_counts = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
    return sort_counts[0][0]


def row_list(row_dataset):
    row_list = []
    for index, rows in row_dataset.iterrows():
        row_list.append(
            [rows.Id, rows.SepalLengthCm, rows.SepalWidthCm, rows.PetalLengthCm, rows.PetalWidthCm]
        )
    return row_list


def set_obs_k(k_count, data, dev_data, test_list, mean, std):
    set_obs_k = {}
    for k in range(1, k_count):
        set_obs = []
        for i in range(len(test_list)):
            set_obs.append(
                knn(data, dev_data, test_list[i], k, mean, std)
            )
        set_obs_k[k] = set_obs
    return set_obs_k


if __name__ == '__main__':
    data = read_data()

    divided_dataset = divide_dataset(data)
    development_set = divided_dataset[0]
    test_set = divided_dataset[1]

    test_list = row_list(test_set)

    mean = data.mean(numeric_only=True)
    std = data.mean(numeric_only=True)

    k_count = int(np.sqrt(len(data) + 1))
    test_set_obs_k = set_obs_k(30, data, development_set, test_list, mean, std)
    # test_set_obs_k = {}
    # for k in range(1, k_count):
    #     test_set_obs = []
    #     for i in range(len(test_list)):
    #         test_set_obs.append(
    #             knn(data, development_set, test_list[i], k, mean, std)
    #         )
    #     test_set_obs_k[k] = test_set_obs

    test_class = list(test_set.iloc[:, -1])
    accuracy = {}

    for k in test_set_obs_k.keys():
        count = 0
        for i,j in zip(test_class, test_set_obs_k[k]):
            if i == j:
                count = count + 1
            else:
                pass
        accuracy[k] = count / len(test_class)

    for k in accuracy.keys():
        print('k =', k, ', accuracy =', accuracy[k])

    best_accuracy = max(accuracy.items(), key=operator.itemgetter(1))
    best_k = best_accuracy[0]
    print(best_k)

















