# GeometricMovingAverageDM.py
import numpy as np
import math
import matplotlib.pyplot as plt
from stream import no_stream as stream

# Plot
plt.autoscale()
plt.xlim(0, len(stream) * 1.5)

# Parâmetros
min_n_instancias = 30
_lambda = 0.3         # Padrão=1, mas é alto para os drifts gerados pelo MOA
_alpha = 0.99

# Atributos
n_instancias = 1.0
media = 0.0
somatorio = 0.0

x, y, drifts = [], [], []

for posicao, valor in enumerate(stream):
    media = media + (valor - media) / n_instancias
    somatorio = _alpha * somatorio + (1.0 - _alpha) * (valor - media)
    
    n_instancias +=1 

    x.append(posicao)
    y.append(media)

    if n_instancias <= min_n_instancias:
        continue
    
    if somatorio > _lambda:
        drifts.append(posicao)
        
        # reset
        n_instancias = 1.0
        media = 0.0
        somatorio = 0.0

# plot
plt.plot(x, y, 'r-', linewidth=0.33)
for posicao in drifts:
    print(posicao)
    plt.axvline(x=posicao, color='k', linestyle=':', linewidth=0.5)
plt.show(block=True)