import sys

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def print_matrix(matrix):
    print(np.array(matrix))


def generate_graph(n):
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            if np.random.randint(0, 2) == 1:
                matrix[i][j] = matrix[j][i] = np.random.randint(0, 100)
    return matrix


def draw_graph(G, n, pos):
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    node_labels = {}
    for i in range(n):
        node_labels[i] = i + 1
    nx.draw_networkx_labels(G, pos, node_labels)
    plt.show()


def graph_connected(graph):
    G = nx.from_numpy_matrix(graph)
    return nx.is_connected(G)


def build_min_graph(matrix, n):
    min_matrix = np.zeros((n, n))

    min_value = sys.maxsize
    min_i = 0
    min_j = 0
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0 and matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_i = i
                min_j = j

    min_matrix[min_i][min_j] = min_matrix[min_j][min_i] = min_value
    connected_nodes = [min_i, min_j]

    while not graph_connected(min_matrix):
        min_value = sys.maxsize
        for i in range(n):
            if not i in connected_nodes:
                for j in connected_nodes:
                    if matrix[i][j] != 0 and matrix[i][j] < min_value:
                        min_value = matrix[i][j]
                        min_i = i
                        min_j = j

        min_matrix[min_i][min_j] = min_matrix[min_j][min_i] = min_value
        connected_nodes.append(min_i)

        if len(connected_nodes) == n and not graph_connected(min_matrix):
            # print_matrix(min_matrix)
            # G = nx.from_numpy_matrix(min_matrix)
            # draw_graph(G, n)
            raise ValueError('graph connect error')

    return min_matrix


def cut_min_graph(matrix, n):
    max_value = 0
    min_i = 0
    min_j = 0
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0 and matrix[i][j] > max_value:
                max_value = matrix[i][j]
                min_i = i
                min_j = j

    matrix[min_i][min_j] = matrix[min_j][min_i] = 0
    return matrix


def run():
    n = 6
    matrix = generate_graph(n)
    while not graph_connected(matrix):
        matrix = generate_graph(n)
    G = nx.from_numpy_matrix(matrix)
    pos = nx.spring_layout(G, seed = 7)
    draw_graph(G, n, pos)

    min_matrix = build_min_graph(matrix, n)
    G = nx.from_numpy_matrix(min_matrix)
    draw_graph(G, n, pos)

    cut_matrix = cut_min_graph(min_matrix, n)
    G = nx.from_numpy_matrix(cut_matrix)
    draw_graph(G, n, pos)


if __name__ == '__main__':
    run()