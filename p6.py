import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mt 
import pandas as pd
import numpy as np

titanic = pd.read_csv("C:/Users/utsav/OneDrive/Desktop/Python-Material/Datasets/titanic.csv")
titanic.info

print(titanic.Survived.value_counts())
print(plt.style.available)

data = titanic.Survived.value_counts()
print(data.plot.bar(color =['aquamarine','lightblue']))

print(plt.style.use('fivethirtyeight'))
data = titanic.Survived.value_counts()

print(plt.figure(figsize = (10,7)))
print(plt.title('Survived Vs Dead',fontsize = 20))
fig = data.plot.bar(color = ['aquamarine','lightblue'])

print(plt.xlabel('Survived', fontsize = 15))
print(plt.ylabel('Count', fontsize = 15))
print(plt.ylim(0,650))
print(plt.xticks([0,1],['Dead','Survived'],rotation = 45, fontsize = 12))
print(plt.yticks(np.arange(0,650,50)))
print(plt.annotate(data[0], xy = (-0.05, data[0]+5, fontsize = 14)))
print(plt.annotate(data[0], xy = (0.95, data[1]+5, fontsize = 14)))
# plt.show()
