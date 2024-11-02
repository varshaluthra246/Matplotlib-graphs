import matplotlib.pyplot as plt
info=['gold','silver','bronze','total']
a=[80,59,59,198]
i=[26,20,20,66]
plt.bar(info,a)
plt.bar(info,i)
plt.xlabel("medal type")
plt.ylabel("a/i medal count")
plt.show()
