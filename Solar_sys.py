import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
    return x

x1 = np.arange(0.0, 5.0, 0.1)
x2 = np.arange(0.0, 5.0, 0.02)

plt.plot(f)
plt.axis([0, 5, 0, 5])
plt.show()
