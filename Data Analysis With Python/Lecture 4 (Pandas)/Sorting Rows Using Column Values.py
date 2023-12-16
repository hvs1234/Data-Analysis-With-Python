from urllib.request import urlretrieve
import pandas as pd

urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 'locations.csv')

urlretrieve('https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv','italy-covid-daywise.csv')

covid_df = pd.read_csv('italy-covid-daywise.csv')

print(f"{covid_df.sort_index(ascending=True)}")

print(f"{covid_df.sort_values('new_cases',ascending=False).head(10)}")
print(f"{covid_df.sort_values('new_deaths',ascending=False).head(10)}")
