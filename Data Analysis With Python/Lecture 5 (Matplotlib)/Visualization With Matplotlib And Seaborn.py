from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from urllib.request import urlretrieve

urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 'locations.csv')

urlretrieve('https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv','italy-covid-daywise.csv')

covid_df = pd.read_csv('italy-covid-daywise.csv')

# plt.plot(covid_df.new_cases,color='b')
# plt.plot(covid_df.new_deaths,color='g')
# plt.plot(covid_df.new_tests,color='r')
# plt.show()

# print(f"{covid_df}")

year = np.arange(2010,2018)
apples = [0.895,0.912,0.919,0.926,0.929,0.931,0.945,0.987]
oranges = [0.962,0.942,0.932,0.918,0.908,0.901,0.876,0.834]

plt.plot(year,apples,color='r',linestyle='solid',marker='o',lw=2,mec='red',mew=2,ms=10)
plt.plot(year,oranges,color='b',linestyle='solid',marker='x',lw=2,mec='blue',mew=2,ms=10)

plt.xlabel('Year')
plt.ylabel('Yield of apples and oranges (in hectare)')
plt.legend(['Apples','Oranges'])

plt.show()

