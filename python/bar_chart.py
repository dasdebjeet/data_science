import matplotlib.pyplot as plt

data = {'Java':22.2, 'Pyhton':17.6, 'PHP':8.8, 'JavaScript':8, 'C#':7.7, 'C++':6.7}
programming_lan = list(data.keys())
popularity = list(data.values())

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
plt.bar(programming_lan, popularity, color=colors, width = 0.5)
plt.xlabel('Programming Language')
plt.ylabel('Popularity')
plt.show()
plt.savefig("E:\Data Science\python\sample.png", dpi=100)