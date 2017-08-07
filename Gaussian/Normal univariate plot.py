import numpy as np
from matplotlib import pyplot as plt

mean = 0
variance = 0.3
standard_deviation = np.sqrt(variance)

x = np.linspace(-3 * standard_deviation, 3 * standard_deviation, 500)
Gaussian = (1 / np.sqrt(2 * np.pi * variance)) * np.exp(-(x - mean)**2 / (2 * variance))

plt.plot(x, Gaussian)
plt.show()
