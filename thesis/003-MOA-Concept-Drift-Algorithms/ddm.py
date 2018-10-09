# ddm.py
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import animation
from stream import abrupt_stream as stream

# Plot
plt.ylim(-1.1, 1.1)

# Parâmetros
min_n_instancias = 30
nivel_alerta = 2.0
nivel_fora_controle = 3.0

# Algoritmo
n_instancias = 1
media = 1
media_quadratica = 0
min_media = float("inf")
min_media_quadratica = float("inf")
min_soma_medias = float("inf")

x,y, drifts = [], [], []

for posicao, valor in enumerate(stream):
    media = media + (valor - media) / n_instancias
    media_quadratica = math.sqrt(media * (1 - media) / n_instancias)

    n_instancias += 1

    # plot
    x.append(posicao)
    y.append(media)

    if n_instancias <= min_n_instancias: 
        continue
    
    if media + media_quadratica <= min_soma_medias:
        min_media = media
        min_media_quadratica = media_quadratica
        min_soma_medias = media + media_quadratica
    
    if n_instancias > min_n_instancias and media + media_quadratica > min_media + nivel_fora_controle * min_media_quadratica:
        # drift
        drifts.append(posicao)

        # reset
        n_instancias = 1
        media = 1
        media_quadratica = 0
        min_media = float("inf")
        min_media_quadratica = float("inf")
        min_soma_medias = float("inf")

# plot
plt.plot(x, y, 'r-', linewidth=0.5)
for posicao in drifts:
    plt.axvline(x=posicao, color='k', linestyle='-', linewidth=0.5)
plt.show(block=True)