# stepd.py
import numpy as np
import math
import matplotlib.pyplot as plt
from stream import abrupt_stream as stream
import scipy.stats

# Plot
plt.autoscale()

# Parâmetros
tamanho_janela = 30
alpha_drift = 0.003
predicoes = [0] * tamanho_janela

# reset
primeira_pos = 0
ultima_pos = -1
acertos_o = 0
acertos_r = 0
erros_o = 0
erros_r = 0
n_instancias_o = 0
n_instancias_r = 0
p, z, soma_invertida = 0, 0, 0
# /reset

# Algoritmo
_ninstancias = 0
_soma = 0
_media = 0

x, y, drifts = [], [], []

for posicao, valor in enumerate(stream):

    if n_instancias_r == tamanho_janela:
        erros_o += predicoes[primeira_pos]
        n_instancias_o += 1

        erros_r -= predicoes[primeira_pos]
        primeira_pos += 1

        if primeira_pos == tamanho_janela:
            primeira_pos = 0
    else:
        n_instancias_r += 1

    ultima_pos += 1
    if ultima_pos == tamanho_janela:
        ultima_pos = 0

    predicoes[ultima_pos] = valor
    erros_r += valor

    _ninstancias += 1
    _soma += valor
    _media = _soma / _ninstancias

    if _ninstancias % 10 == 0:
        x.append(posicao)
        y.append(_media)

    if n_instancias_o >= tamanho_janela:
        acertos_o = n_instancias_o - erros_o
        acertos_r = n_instancias_r - erros_r

        soma_invertida = 1.0 / n_instancias_o + 1.0 / n_instancias_r
        p = (acertos_o + acertos_r) / (n_instancias_o + n_instancias_r)
        Z = abs(acertos_o / n_instancias_o - acertos_r / n_instancias_r)
        Z = Z - soma_invertida / 2.0
        Z = Z / math.sqrt(p * (1.0 - p) * soma_invertida)
        print(Z)
        Z = scipy.stats.norm.pdf(abs(Z), loc=0.0, scale=0.5)
        Z = 2 * (1 - Z) 
        
        

        if Z < alpha_drift:
            # drift
            drifts.append(posicao)

            # reset
            primeira_pos = 0
            ultima_pos = -1
            acertos_o = 0
            acertos_w = 0
            erros_o = 0
            erros_w = 0
            n_instancias_o = 0
            n_instancias_w = 0

# plot
plt.plot(x, y, "r-", linewidth=0.5)
for posicao in drifts:
    plt.axvline(x=posicao, color="k", linestyle="-", linewidth=0.5)
plt.show(block=True)