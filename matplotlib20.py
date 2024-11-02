import numpy as np
import matplotlib.pyplot as plt
X1 = np.random.randint(1,100, size=(250,))
Y1 = np.random.randint(1,100, size=(250,))
Z1 = np.random.randint(1,100, size=(250,))
size = range(1,60,5)
plt.scatter(X1, Y1, color='r', s=size)
plt.scatter(X1, Z1, color='r', s=size)
plt.show()
