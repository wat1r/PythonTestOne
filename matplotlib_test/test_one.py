from matplotlib import pyplot as plt

plt.figure(figsize=(20, 8), dpi=80)

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]
plt.plot(x, y)

_xtick_labels =[i/2 for i in range(4,49)]
_ytick_labels=range(min(y),max(y)+2)
plt.xticks(_xtick_labels[::3])
plt.yticks(_ytick_labels)

# plt.savefig("./t1.png")

plt.show()
