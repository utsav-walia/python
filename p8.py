corr = df.corr()
print(corr)

import numpy as np
import seaborn as sns

sns.heatmap(corr)

g = sns.Pairgrid(df5)
print(g.map(plt.scatter))
# OR
g = sns.Pairgrid(number)
print(g.map(plt.scatter))


