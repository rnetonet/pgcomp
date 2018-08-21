# Revisão Prova

## Estatística básica que será aplicada:

### `mean` - média simples entre os valores

```python
In [6]: values = [2, 3, 4]
In [7]: mean(values)
Out[7]: 3
```

### `median` - mediana, "o valor do meio"

```python
In [10]: values = [1, 20, 300] # if odd, the middle is returned. no questions asked.
In [11]: median(values)
Out[11]: 20

In [12]: # if even, average of two middles
In [13]: values = [1, 20, 50, 300]
In [14]: median(values)
Out[14]: 35.0
```

### `mode` - moda, "valor mais comum"

```python
In [15]: values = [1, 2, 2, 3, 3, 3, 4]
In [16]: mode(values)
Out[16]: 3

In [17]: values = [1, 1, 1, 2, 3, 4, 5]
In [18]: mode(values)
Out[18]: 1
```

### `variance` - calcula o grau de dispersão dos dados

Um alta variância indica que os valores se dispersam para longe do valor médio. Uma baixa variância indica que os valores ficam pertinhos lá do valor médio, não vão para muito longe.

```python
In [8]: values = [0.1, 0.2, 0.5, 0.7]
In [9]: variance(values)
Out[9]: 0.07583333333333332
```

### `stdev` - é a raíz da variância...vantangem é que tem a mesma unidade que a média, melhor para comparar e tal

```python
In [15]: values = [0.1, 0.2, 0.5, 0.7]

In [16]: variance(values)
Out[16]: 0.07583333333333332

In [17]: stdev(values)
Out[17]: 0.27537852736430507

In [18]: sqrt(variance(values))
Out[18]: 0.27537852736430507 # the same as stdev...
```

## Quanto a formação de clusters:

**Bem Formado**: Elementos do cluster estão mais próximos a outros elementos do mesmo cluster, do que qualquer outro cluster.

**Baseado em centroide**: Elementos do cluster estão mais próximos ao centroide do seu cluster do que o centroide de qualque outro cluster.

**Contínuo ou encadeado**: Elementos do cluster estão mais próximos a um ou mais vizinhos do mesmo cluster do que qualquer outro elemento de outro cluster.

**Baseado em similaridade**: Cluster é formado por dados muito similares entre si. Clusters diferentes, dados bastante diferentes.


## Critérios da validação

### Índices

* **Variância intracluster**: Verifica o grau de compactação dos grupos. Intervalor [0, inf]. Quanto menor, melhor, maior a compactação, menor dispersão.

* **Conectividade**: Verifica o grau com que vizinhos mais próximos são colocados no mesmo grupo. Intervalor [0, inf]. Quanto menor, melhor o agrupamento.

* **Dunn**: Mede a separação intracluster e entre clusters. Quanto maior o valor, melhor.

* **Silhueta**: Baseado na similaridade entre objetos de um mesmo cluster e a distância entre objetos de um cluster para os objetos de um outro cluster próximo.

Intervalor: [-1, 1].

Quanto mais próximo de 1, maior distância para outros objetos de outro cluster, melhor.

É o mais utilizado. Pois o índice independe de algoritmo, apenas das partições formadas. É usado para analisar resultados e comparar entre algoritmos.

### Medidas de Similaridade

#### Medidas de distância:

* Quanto menor a distância entre dois atributos, mais similares os objetos;
* Deve-se normalizar os dados, entre [0, 1];
    * Se `similaridade(X, Y) == 1, X == Y`
    * Se `similaridade(X, Y) == 0, X != Y`

* Cuidado para não comparar atributos que não têm nada a ver;

* **Distância Euclidiana**:

É a distância usando o clássico teorema de Pitágoras.

```
1) Recebe dois pontos;
2) Compara a diferença (primeiro - segundo) de cada eixo entre os pontos;
3) Eleva essa diferença ao quadrado e adiciona a um somatório;
4) Ao final, retorna a raíz quadrada do somatório.
```

```python
from math import *
 
In [16]: def euclidean(x, y):
    ...:     soma = 0
    ...: 
    ...:     # Compara x[0], y[0]; x[1], y[1]
    ...:     for a, b in zip(x, y):
    ...:         # calcula a diferenca
    ...:         diferenca = a - b
    ...: 
    ...:         # eleva a diferenca
    ...:         diferenca2 = pow(diferenca, 2)
    ...:         soma += diferenca2
    ...: 
    ...:     # retorna a raiz da soma total
    ...:     return sqrt(soma)
    ...: 
    ...: 

In [17]: euclidean([0,3,4,5],[7,6,3,-1])
Out[17]: 9.746794344808963
```

* **Manhattan**:

Similar à euclidiana, pois compara os eixos dos dois pontos.
Mas retorna ao final a soma das diferenças absolutas.

```
1) Recebe dois pontos;
2) Calcula a diferença absoluta (|primeiro - segundo|) de cada eixo entre os pontos;
3) Adiciona essa diferença a um somatório
4) Retorna o valor do somatório
```

```python
In [20]: def manhattan(x, y):
    ...:     soma = 0
    ...: 
    ...:     for i in range(len(x)):
    ...:         diferenca = abs(x[i] - y[i])
    ...:         soma += diferenca
    ...:     
    ...:     return soma
    ...: 
    ...: 

In [21]: manhattan([10,20,10],[10,20,20])
Out[21]: 10
```

## Algoritmos

### K-Means

Algoritmo recebe uma matriz e **k**, o número de grupos a serem formados.

```
1) Define aleatoriamente K centróides para os futuros clusters;
2) Cada objeto é associado ao cluster com centróide mais próximo;
3) Centróides são recalculados de acordo com os objetos mais próximos;
4) Algoritmo para quando não houver mudança nos centróides.
```

```python
import math
import random
import statistics

import matplotlib
import matplotlib.pyplot as plt
import numpy

def euclidean(x, y):
    return math.sqrt( sum(pow(a-b, 2) for a, b in zip(x, y)) )

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
            if point in clusters.keys(): continue

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

if __name__ == '__main__':
    # Gerando pontos aleatórios
    data = []

    for _ in range(20):
        point = (random.randint(0, 20), random.randint(0, 20))
        random.seed()
        if point not in data: data.append(point)
    
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
```

### Hierárquico - HCluster

```
1) Recebe um dataset com N dados e cria um cluster para cada um dos dados, obtendo N clusters;
2) Encontre os dois clusters mais próximos e faça o merge deles. Um cluster a menos;
3) Calcule a distância desse novo cluster em relação aos antigos. 
4) Repita os passos 2 e 3 até todos itens estarem em um único cluster, com N elementos.
```

**Como calcular a distância ?** A distância entre os clusters que irão sofrer merge pode ser feita de diversas formas:

* **Single-link**: Menor distância entre dois pontos quaisquer dos clusters. Um de cada;

> Mais sujeito a ruídos e outliers.

* **Average-link**: Distância média entre os pontos dos dois clusters;

* **Complete-link**: Distância máxima entre dois pontos quaisquer dos clusters;

> Menos sucetível a outliers e ruídos, mas prefere formatos 

* **Centroid-link**: Menor distância entre os centróides dos clusters.


```python
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
```

### Fuzzy C-Means

* Padrões pertencem a mais de um cluster por vez;
* Gera agrupamentos, mas não produz uma partição;
* Cada cluster contém todos padrões e seus graus de pertencimentos;
* Como saber se a pseudo-partição formada é boa ? **Índice de Desempenho**. Um índice que calcula (soma ponderada) a compactação dos grupos em relação a seus centróides. Objetivo é diminuir o valor do índice, aumentando a compactação dos grupos.


```python

```