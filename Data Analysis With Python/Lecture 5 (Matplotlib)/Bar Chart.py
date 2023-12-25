from matplotlib import pyplot as plt
import numpy as np

years = np.arange(2000,2006)
apples = [0.35,0.6,0.9,0.8,0.65,0.8]
oranges = [0.4,0.8,0.9,0.7,0.6,0.8]

plt.title('Distribution of apples and oranges')
plt.bar(years,apples,color='r')
plt.bar(years,oranges,color='b',bottom=apples)
plt.show()
