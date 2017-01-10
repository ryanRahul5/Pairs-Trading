# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 17:20:07 2016

@author: Rahul
"""
import numpy as np
import statsmodels.api as sm
import pandas as pd

import statsmodels
from statsmodels.tsa.stattools import coint

import matplotlib.pyplot as plt




data = pd.read_csv('C:\Users\Dell\Desktop\Pairs Trading\FuturePrices.csv', parse_dates = 'Date', index_col = 'Date')

X = data['ADANIPOWER']
Y = data['JSWENERGY']

Y.tail(5)
X = X['2014-01-01': '2014-12-31']
Y = Y['2014-01-01': '2014-12-31']

pd.concat([X, Y], axis=1).plot()

(Y/X).plot()
plt.axhline((Y/X).mean(), color='red', linestyle='--')

score, pvalue, _ = coint(X,Y)
print pvalue

def zscore(series):
    return (series - series.mean()) / np.std(series)

ratio_series = Y/X
zscore(ratio_series).plot()
plt.axhline(zscore(ratio_series).mean(), color='black')
plt.axhline(1.0, color='red', linestyle='--')
plt.axhline(-1.0, color='green', linestyle='--')


ratio = Y / X
ratio.name = 'ratio'

# Get the 10 day moving average of the difference
#diff_mavg10 = pd.rolling_mean(difference, window=10)
#diff_mavg10.name = 'diff 10d mavg'

# Get the 60 day moving average
ratio_mavg60 = pd.rolling_mean(ratio, window=60)
ratio_mavg60.name = 'ratio 60d mavg'

std_60 = pd.rolling_std(ratio, window=60)
std_60.name = 'std 60d'

# Compute the z score for each day
zscore_60 = (ratio - ratio_mavg60)/std_60
zscore_60.name = 'z-score'
zscore_60.plot()
plt.axhline(0, color='black')
plt.axhline(1.5, color='red', linestyle='--')
plt.axhline(-1.5, color='green', linestyle='--')





















