import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
x=[2,4,6,8]
y=[7,3,8,3]
x2=[1,3,5,7]
y2=[6,7,2,6]
plt.bar(x,y,color='c',align= 'center')
plt.bar(x2,y2,color='g',align= 'center')
plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.plot(x,y)
plt.plot(x2,y2)
plt.show()
