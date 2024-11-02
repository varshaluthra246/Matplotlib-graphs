import numpy as np
import matplotlib.pyplot as plt
data = [[5.,25.,45.,20.,],[8.,13.,29.,27.],[9.,29.,27.,39.]]
x=np.arange(4)
plt.plot(x, data[0], color = 'b', label = 'range1')
plt.plot(x, data[1], color = 'g', label = 'range2')
plt.plot(x, data[2], color = 'r', label = 'range3')
plt.legend(loc = 'upper left')
plt.title("Mutlirange Line chart")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
