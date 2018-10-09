# eddm.py
import numpy as np
import math
import matplotlib.pyplot as plt
from stream import abrupt_stream as stream

# Plot
plt.autoscale()
plt.xlim(0, len(stream) * 1.5)

# Parâmetros
nivel_fora_controle = 0.9
nivel_alerta = 0.95
min_n_instancias = 30
min_n_erros = 30

# Algoritmo
n_instancias = 1    # m_n
n_erros = 0         # m_numErrors
m_d = 0
m_lastd = 0
media = 0.0         # m_mean
desvio_padrao_temp = 0.0 # m_stdTemp
max_media_x_desvio = 0.0

x, y, drifts = [], [], []

for posicao, valor in enumerate(stream):
    n_instancias += 1

    if valor == 1.0:
        n_erros += 1
        m_lastd = m_d
        m_d = n_instancias - 1
        distancia = m_d - m_lastd
        media_anterior = media
        media = media + (distancia - media) / n_erros
        desvio_padrao_temp = desvio_padrao_temp + (distancia - media) * (distancia - media_anterior)
        desvio_padrao =  math.sqrt(desvio_padrao_temp / n_erros)
        media_x_desvio = media + 2 * desvio_padrao

        # plot
        x.append(posicao)
        y.append(media)

        if media_x_desvio > max_media_x_desvio:
            if n_instancias > min_n_instancias:
                max_media_x_desvio = media_x_desvio
        else:
            p = media_x_desvio / max_media_x_desvio
            if n_instancias > min_n_instancias and n_erros > min_n_erros and p < nivel_fora_controle:
                # drift
                drifts.append(posicao)              

                # reset
                n_instancias = 1    # m_n
                n_erros = 0         # m_numErrors
                m_d = 0
                m_lastd = 0
                media = 0.0         # m_mean
                desvio_padrao_temp = 0.0 # m_stdTemp
                max_media_x_desvio = 0.0
    
    
    
# plot
plt.plot(x, y, 'r-', linewidth=0.5)
for posicao in drifts:
    plt.axvline(x=posicao, color='k', linestyle='-', linewidth=0.5)
plt.show(block=True)