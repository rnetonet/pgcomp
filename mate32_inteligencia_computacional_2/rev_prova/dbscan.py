import math
import random
import statistics

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def dbscan(data, eps, minpts):
    """
        data   -> list of vectors
        eps    -> threshold distance
        minpts -> 
    """
    #
    # Variável que guarda o mapeamento de cada instância
    # -1 => noise
    # 0  => não visitado
    # X  => número do cluster
    #
    mapeamento = [0] * len(data)

    cluster_atual = 0

    # Encontrando pontos núcleo
    for instancia_idx in range(0, len(data)):
        # Se já foi visitado, pula
        if mapeamento[instancia_idx] != 0:
            continue

        vizinhos = coletar_vizinhos(data, instancia_idx, eps)

        # Se não tem vizinhos suficientes, noise
        if len(vizinhos) < minpts:
            mapeamento[instancia_idx] = -1
        else:
            cluster_atual += 1
            expanda_cluster(
                data, mapeamento, instancia_idx, vizinhos, cluster_atual, eps, minpts
            )

    # Retorna o mapeamento
    return mapeamento


def expanda_cluster(data, mapeamento, i, vizinhos, cluster_atual, eps, minpts):
    # Marca a instância passada como integrante de cluster_atual
    mapeamento[i] = cluster_atual

    # Para cada vizinho
    j = 0
    while j < len(vizinhos):
        vizinho = vizinhos[j]

        # Se vizinho foi marcado como noise
        # Corrige, ele é borda
        if mapeamento[vizinho] == -1:
            mapeamento[vizinho] == cluster_atual

        # Se o vizinho não foi visitado ainda
        elif mapeamento[vizinho] == 0:
            mapeamento[vizinho] = cluster_atual

            vizinhos_de_j = coletar_vizinhos(data, vizinho, eps)

            # Adiciona os vizinhos de j a lista de visita
            if len(vizinhos_de_j) >= minpts:
                vizinhos = vizinhos + vizinhos_de_j

        j += 1


def coletar_vizinhos(data, instancia_idx, eps):
    vizinhos = []

    for idx in range(0, len(data)):
        if np.linalg.norm(data[instancia_idx] - data[idx]) < eps:
            vizinhos.append(idx)

    return vizinhos


if __name__ == "__main__":
    data = np.random.randint(100, size=(50, 2))

    particao = dbscan(data, 15, 3)

    print(data)
    print(particao)

    # Plotando
    cores = {
        -1: "Grey",
        0: "Red",
        1: "Green",
        2: "Yellow",
        3: "Blue",
        4: "Orange",
        5: "Purple",
        6: "Cyan",
        7: "Magenta",
        8: "Lime",
        9: "Pink",
        10: "Teal",
        11: "Lavender",
        12: "Brown",
        13: "Beige",
        14: "Maroon",
        15: "Mint",
        16: "Olive",
        17: "Coral",
        18: "Navy",
        19: "Black",
        20: "White",
    }

    for index, cluster_id in enumerate(particao):
        plt.scatter(data[index][0], data[index][1], c=cores[cluster_id], alpha=1)

    plt.show()
