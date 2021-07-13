# -*- coding: utf-8 -*-
"""MLR Error_opt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PEXdV_5S4ym17D_G0FBH_u9VoS-pSvN5
"""

import pandas as pd

df = pd.read_csv("/content/Advertising.csv")

df

x = df.iloc[:,0:3].values    # All 3 features
y = df.iloc[:,3].values

x = df.iloc[:,0].values.reshape(-1,1) # TV feature alone

x = df.iloc[:,0:2].values    # TV and Radio features

x

x.shape

from sklearn.linear_model import LinearRegression

Lin = LinearRegression()

Lin.fit(x,y)

pred_y = Lin.predict(x)

from sklearn import metrics

metrics.mean_absolute_error(y, pred_y)    # All 3 features

metrics.mean_absolute_error(y, pred_y) # TV feature alone

metrics.mean_absolute_error(y, pred_y) # TV and Radio

df.corr()

