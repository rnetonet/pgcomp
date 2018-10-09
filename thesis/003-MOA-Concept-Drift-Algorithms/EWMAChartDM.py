# EWMAChartDM.py
import numpy as np
import math
import matplotlib.pyplot as plt
from stream import abrupt_stream as stream

# Plot
plt.autoscale()
plt.xlim(0, len(stream) * 1.5)

# Parâmetros
_lambda = 0.2
min_n_instancias = 30

# Atributos
n_instancias = 1.0
somatorio = 0.0
media = 0.0
media_quadratica = 0.0
z_t = 0.0

x, y, drifts = [], [], []

for posicao, valor in enumerate(stream):
    somatorio += valor
    media = somatorio / n_instancias
    media_quadratica = math.sqrt( media * (1.0 - media) * _lambda * (1.0 - math.pow(1.0 - _lambda, 2.0 * n_instancias)) / (2.0 - _lambda) )
    n_instancias += 1
    z_t += _lambda * (valor - z_t)
    l_t = 3.97 - 6.56 * media + 48.73 * math.pow(media, 3) - 330.13 * math.pow(media, 5) + 848.18 * math.pow(media, 7)
    
    x.append(posicao)
    y.append(media)

    if n_instancias <= min_n_instancias:
        continue
    
    if z_t > media + l_t * media_quadratica:
        drifts.append(posicao)
        
        # reset
        n_instancias = 1.0
        somatorio = 0.0
        media = 0.0
        media_quadratica = 0.0
        z_t = 0.0

# plot
plt.plot(x, y, 'r-', linewidth=0.5)
for posicao in drifts:
    print(posicao)
    plt.axvline(x=posicao, color='k', linestyle='-', linewidth=0.5)
plt.show(block=True)