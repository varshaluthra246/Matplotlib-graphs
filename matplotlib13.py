import matplotlib.pyplot as plt
info = ['gold','Silver','Bronze','Total']
A=[80,59,59,198]
I=[26,20,20,66]
plt.bar(info,A)
plt.bar(info,I)
plt.xlabel("Medals")
plt.ylabel("A Vs I")
plt.show()


