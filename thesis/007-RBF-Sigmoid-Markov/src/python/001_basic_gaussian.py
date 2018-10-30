import matplotlib.pyplot as plt
import numpy as np

def ga(x, a, b, c):
    """
    Gaussian

    a = curve_peak_height
    b = curve_center_position
    c = bell_width
    """
    return a * (np.e ** -( (x-b)**2 / (2 * (c ** 2)) ))

# curve_peak_height
a = 100

# curve_center_position
b = 50

# bell_width
c = 10

plt.plot([ga(x, a, b, c) for x in np.arange(0, 101)])
plt.show()