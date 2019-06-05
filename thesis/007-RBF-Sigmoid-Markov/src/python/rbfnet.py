import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate

from markov import Markov

# Params
sigma = 2
threshold = 0.3

# Variables
centers = []
actual_center = None

# Plot init
plt.autoscale()
colors = "bgrcmykw"
x = []
y = []
drifts = []

# Abrupt TS
ta = np.random.uniform(0, 5, 3)
tb = np.random.uniform(10, 15, 3)

timeserie = np.concatenate((ta, ta, ta, tb, ta, ta))

table = []
headers = ["Input", "Center", "Activation", "Threshold"]

for index, input_data in enumerate(timeserie):
    row = []
    row.append(input_data)

    # plot
    x.append(index)
    y.append(input_data)

    # some center activates ?
    activation_threshold = threshold
    activated_center = None
    activation = 0.0

    for center in centers:
        distance = np.sqrt(np.float_power(input_data - center, 2))
        activation = np.exp(
            # ϕ(r) = exp(- r²/2σ²)
            -(np.float_power(distance, 2.0))
            / (2.0 * np.float_power(sigma, 2.0))
        )

        table.append(
            [input_data, center, format(activation, '.4f'), format(activation_threshold, '.4f')]
        )

        if activation >= activation_threshold:
            activated_center = center
            activation_threshold = activation

    # no center activates, so we have a new center
    if activated_center is None:
        centers.append(input_data)
        activated_center = input_data

    # if no center had been activated before
    if actual_center is None:
        actual_center = input_data

    # if actual_center is not the activated_center, drift, drift!
    if actual_center != activated_center:
        actual_center = activated_center
        drifts.append(index)

    plt.plot(
        index,
        input_data,
        "ro",
        linewidth=0.5,
        color=colors[centers.index(actual_center)],
    )

print(tabulate(table, headers, tablefmt="grid"))

# Plot
for index in drifts:
    plt.axvline(x=index, color="k", linestyle="-", linewidth=0.5, label="drift")
plt.show(block=True)
