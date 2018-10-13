# cusumdm.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from stream import abrupt_stream as stream

# Plot
plt.autoscale()

# Parâmetros
min_instancias = 30
redutor = 0.005
limite = 50.0

# Algoritmo
n_valores = 1
media = 0
soma = 0

_ninstancias = 0
_soma = 0
_media = 0

x,y, drifts = [], [], []

for posicao, valor in enumerate(stream):
    media = media + (valor - media) / n_valores
    soma = max(0, soma + valor - media - redutor)
    n_valores += 1

    # plot
    _ninstancias += 1
    _soma += valor
    _media = _soma / _ninstancias

    if _ninstancias % 10 == 0:
        x.append(posicao)
        y.append(_media)
    
    if n_valores >= min_instancias and soma > limite:
        # drift
        drifts.append(posicao)

        # reset
        n_valores = 1
        media = 0
        soma = 0

# plot
plt.plot(x, y, 'r-', linewidth=0.5)
for posicao in drifts:
    print(posicao)
    plt.axvline(x=posicao, color='k', linestyle='-', linewidth=0.5)
plt.show(block=True)