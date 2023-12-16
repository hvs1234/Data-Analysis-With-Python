from urllib.request import urlretrieve
import pandas as pd

urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 'locations.csv')

urlretrieve('https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv','italy-covid-daywise.csv')

covid_df = pd.read_csv('italy-covid-daywise.csv')

# print(f"{covid_df}","\n")

covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day

covid_month_df = covid_df.groupby('month')[['new_cases','new_deaths','new_tests']]
# print(f"{covid_month_df}","\n")

covid_month_mean_df = covid_df.groupby('day')[['new_cases','new_deaths','new_tests']].mean()
print(f"{covid_month_mean_df}","\n")