from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

plt.figure(figsize=(12,6))
flights = sns.load_dataset("flights").pivot(index="month", columns="year", values="passengers")
sns.heatmap(flights,annot=True,fmt="d",cmap='Blues')
plt.show()
# print(f"{flights_df}")