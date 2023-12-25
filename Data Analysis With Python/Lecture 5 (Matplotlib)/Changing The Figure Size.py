import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

year = np.arange(2010,2018)
apples = [0.895,0.912,0.919,0.926,0.929,0.931,0.945,0.987]
oranges = [0.962,0.942,0.932,0.918,0.908,0.901,0.876,0.834]

plt.figure(figsize=(8,6))

sns.set_style('whitegrid')

plt.plot(year,apples,lw=2,marker='o',mec='red',color='red',mew=2,ms=10)
plt.plot(year,oranges,lw=2,marker='x',mec='green',color='green',mew=2,ms=10)

plt.xlabel('Year')
plt.ylabel('Yield of apples and oranges (in hectare)')
plt.legend(['Apples','Oranges'])

plt.show()  