import math
import random
import statistics

import matplotlib
import matplotlib.pyplot as plt
import numpy


def euclidean(x, y):
    return math.sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))


def kmeans(data, k=2, niter=10):
    # Escolha aleatória dos centróides iniciais
    centroids = random.sample(data, k)

    while niter:
        # Mantendo os clusters formados em um dicionário
        clusters = {}
        for centroid in centroids:
            clusters[centroid] = []

        # Qual o centróide mais próximo para cada ponto ?
        # Bota o ponto no cluster desse centróide
        for point in data:
            if point in clusters.keys():
                continue

            closer_centroid = centroids[0]

            for centroid in centroids:
                if euclidean(centroid, point) < euclidean(closer_centroid, point):
                    closer_centroid = centroid

            clusters[closer_centroid].append(point)

        # Faz um novo cálculo dos centróides
        old_clusters = clusters.copy()

        centroids = []
        for centroid, points in old_clusters.items():
            new_centroid = tuple(map(numpy.mean, zip(*points)))
            centroids.append(new_centroid)

        niter -= 1

    return clusters


if __name__ == "__main__":
    # Gerando pontos aleatórios
    data = []

    for _ in range(20):
        point = (random.randint(0, 20), random.randint(0, 20))
        random.seed()
        if point not in data:
            data.append(point)

    # Executando kmeans
    clusters = kmeans(data, k=2)

    # Imprimindo
    for centroid, points in clusters.items():
        print(centroid, points)

    # Plotando
    colors = ["red", "green"]
    ncolor = 0
    for cluster, points in clusters.items():
        plt.scatter(cluster[0], cluster[1], s=[300], c=colors[ncolor], alpha=0.5)

        for point in points:
            plt.scatter(point[0], point[1], c=colors[ncolor], alpha=0.5)

        ncolor += 1

    plt.show()
