from urllib.request import urlretrieve
import pandas as pd

urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 'locations.csv')

urlretrieve('https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv','italy-covid-daywise.csv')

covid_df = pd.read_csv('italy-covid-daywise.csv')

total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()
total_tests = covid_df.new_tests.sum()

print(f"{covid_df}","\n")

print(f"Total Cases = {total_cases}","\n"); print(f"Total Deaths = {total_deaths}","\n")

print(f"Total death rate = Total sum of new death cases / Total sum of new test cases = {total_deaths / total_cases}","\n")

initial_tests = 935310
print(f"Total Tests = {initial_tests + total_tests}","\n")

print(f"Positive rate = {total_cases / total_tests}","\n")