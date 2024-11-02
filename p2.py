import matplotlib.pyplot as plt
col = [8000,12000, 9800, 11200, 15500, 7300]
section = ['A','B','C','D','E','F']
expl =[0,0,0.15, 0, 0.2, 0]
colr= ['cyan', 'gold', 'violet', 'lightgreen', 'pink','silver'] 
plt.title = ("volunteering week collection")
plt.axis('equal')
plt.pie(col, labels = section, explode=expl, colors=colr,autopct = "%5.2f%%")
plt.show()
