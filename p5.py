import numpy as np
import matplotlib.pyplot as plt
col = [8000,12000, 9800, 11200, 15500, 7300]
x = [1,2,3,4,5,6] 
plt.title = ("volunteering week collection")
plt.xticks(x,['Mon','Tue','Wed','Thu','Fri','Sat'])
plt.xlabel("days")
plt.ylabel('collection')
plt.bar(x, col, color = 'olive', width=0.25)
plt.show()
