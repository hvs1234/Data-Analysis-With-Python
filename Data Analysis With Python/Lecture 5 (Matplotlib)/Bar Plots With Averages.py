import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

tips_df = sns.load_dataset('tips')
# print(f"{tips_df}","\n")
bill_avg = tips_df.groupby('day')[['total_bill']].mean()

plt.bar(bill_avg.index , bill_avg.total_bill)
plt.show()