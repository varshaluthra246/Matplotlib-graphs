import matplotlib.pyplot as plt
plt.figure(figsize = (10,7))
day1 = [74.25, 76.06, 69.5, 70]
day2 = [56.03, 68.71, 62.89, 56.42]
day3 = [50.3, 72.07, 77.65, 66.46]
finlist = [day1, day2, day3]
plt.boxplot(finlist,patch_artist = True, notch = True,  labels = ['day1','day2','day3'])
plt.title("prices")
plt.show()
