import seaborn as sns
from matplotlib import pyplot as plt

flowers_df = sns.load_dataset('iris')

print(f"{flowers_df.species.unique()}")
# print(f"{flowers_df}")
plt.plot(flowers_df.sepal_length, flowers_df.sepal_width)
sns.scatterplot((flowers_df.sepal_length , flowers_df.sepal_width))
# plt.show()

#Adding Hues

plt.plot(flowers_df.sepal_length, flowers_df.sepal_width)
sns.scatterplot((flowers_df.sepal_length , flowers_df.sepal_width),hue=flowers_df.species,s=100)
plt.show()