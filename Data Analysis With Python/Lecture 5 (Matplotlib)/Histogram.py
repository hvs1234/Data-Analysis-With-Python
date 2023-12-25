from matplotlib import pyplot as plt
import seaborn as sns

flowers_df = sns.load_dataset('iris')
# plt.plot(flowers_df.sepal_length,color='r',marker='o',ms='10',mec='red')

plt.title('Distribution of sepal width')
sns.set_style('whitegrid')
plt.hist(flowers_df.sepal_width,bins=5)
plt.show()