import numpy as np
import matplotlib.pyplot as plt
col = [8000,12000, 9800, 11200, 15500, 7300]
x = [1,2,3,4,5,6]
#x = np.arange(6)  #range to signify 6 days 
plt.title = ("volunteering week collection")
#plt.axis('equal')
plt.bar(x, col,  color='r', width=0.25)
plt.xlabel("days")
plt.ylabel('collection')
plt.show()
