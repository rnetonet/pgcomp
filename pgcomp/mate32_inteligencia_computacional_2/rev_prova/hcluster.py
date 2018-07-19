import math
import random
import statistics

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance


def single_link(cluster_a, cluster_b):
    """Retorna a menor distância entre os pontos de dois clusters"""
    distances = []
    for point_a in cluster_a:
        for point_b in cluster_b:
            distances.append(distance.euclidean(point_a, point_b))

    return min(distances)


def hcluster(data):
    partitions = []
    clusters = []

    # Primeira partição: um cluster para cada elemento
    for element in data:
        clusters.append([element])
    partitions.append(clusters)

    # Enquanto a última partição tiver mais de um cluster
    while True:
        last_partition = partitions[-1]

        if len(last_partition) == 1:
            break

        # Vamos descobrir quais os dois clusters mais próximos ?
        current_partition = []

        min_distance = float("inf")
        min_i = 0
        min_j = 0

        for i, cluster_i in enumerate(last_partition):
            for j, cluster_j in enumerate(last_partition):
                if i != j:
                    if single_link(cluster_i, cluster_j) < min_distance:
                        min_distance = single_link(cluster_i, cluster_j)
                        min_i = i
                        min_j = j

        # Coloca todos os outros clusters na nova partição, exceto os dois mais próximos
        for index, cluster in enumerate(last_partition):
            if index not in (min_i, min_j):
                current_partition.append(cluster)

        # Coloca os dois mais próximos juntos como um novo cluster na partição
        current_partition.append(last_partition[min_i] + last_partition[min_j])

        # Adiciona a partição ao dendograma
        partitions.append(current_partition)

    return partitions


if __name__ == "__main__":
    # 5 points  (x, y)
    data = np.random.randint(100, size=(5, 2))

    partitions = hcluster(data)

    for index, partition in enumerate(partitions):
        print("-" * 40)
        print(index, ")")
        for cluster in partition:
            for point in cluster:
                print(point, end=" ")
            print("")
