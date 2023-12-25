from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

flowers_df = sns.load_dataset('iris')

setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor'] 
virginica_df = flowers_df[flowers_df.species == 'virginica'] 

plt.hist([setosa_df.sepal_width,versicolor_df.sepal_width,virginica_df.sepal_width],alpha=0.4,bins=np.arange(2,5,0.25),stacked=True)
# plt.hist(versicolor_df.sepal_width,alpha=0.4,bins=np.arange(2,5,0.25))
# plt.hist(virginica_df.sepal_width,alpha=0.4,bins=np.arange(2,5,0.25))

plt.title('Distribution of flowers')
plt.legend(['Setosa','Versicolor','Virginica'])
plt.show()