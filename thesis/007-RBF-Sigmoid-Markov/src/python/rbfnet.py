import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Plot
plt.autoscale()

# Init
sigma = 1
threshold = 0.55
centers = []
actual_center = None

# Plot
x = []
y = []
drifts = []

for index, input_data in enumerate(np.random.lognormal(size=10)):
    x.append(index)
    y.append(input_data)

    activation_max = threshold
    activated_center = None

    for center in centers:
        distance = np.sqrt(np.float_power(input_data - center, 2))
        activation = np.exp(
            -(np.float_power(distance, 2.0)) / (2.0 * np.float_power(sigma, 2.0))
        )

        if activation > activation_max:
            activated_center = center
            activation_max = activation

    if activated_center is None:
        centers.append(input_data)

    if actual_center is None:
        actual_center = input_data
    else:
        if activated_center is None:
            actual_center = input_data
        elif actual_center != activated_center:
            actual_center = activated_center
            drifts.append(index)

# Plot
plt.plot(x, y, "r-", linewidth=0.5)
for index in drifts:
    plt.axvline(x=index, color="k", linestyle="-", linewidth=0.5, label="drift")
plt.show(block=True)
