from urllib.request import urlretrieve
import pandas as pd

urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 'locations.csv')

urlretrieve('https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv','italy-covid-daywise.csv')

covid_df = pd.read_csv('italy-covid-daywise.csv')

covid_data_dict = {
    'date': ['2020-08-30','2020-08-31','2020-09-01','2020-09-02'],
    'new_cases': [1444,1365,996,975,1326],
    'new_deaths': [1,4,6,8,6],
    'new_tests': [53541,42583,54395,None,None]
}

print(f"{covid_df}","\n")
# print(f"{covid_data_dict}")
# print(f"{covid_data_dict['new_cases']}")

# print(f"{covid_df['new_cases']}")
# print(f"{covid_df['new_cases'][5]}")

# print(f"{type(covid_data_dict)}")
# print(f"{type(covid_data_dict['new_deaths'])}")

# covid_df_copy = covid_df.copy()
# print(f"{covid_df_copy},'\n'")

# print(f"{covid_df.loc[5]}")

print(f"{covid_df.new_cases.first_valid_index()}","\n")
print(f"{covid_df.sample(10)}","\n")