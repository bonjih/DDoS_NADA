from pandas import Series
from pandas import DataFrame
import pandas as pd
from scipy.stats import boxcox
from matplotlib import pyplot


# lambda = -1. is a reciprocal transform.
# lambda = -0.5 is a reciprocal square root transform.
# lambda = 0.0 is a log transform.
# lambda = 0.5 is a square root transform.
# lambda = 1.0 is no transform

# dataset gives Lambda: 0.205324, need to work out if log or sqr is the best


df = pd.read_csv('data/test_pps_rx_1_month_epoch.csv')

series = pd.Series(df['Utilisation pps Rx'])

df = DataFrame(series.values)
df.columns = ['Utilisation pps Rx']
df['Utilisation pps Rx'] = boxcox(df['Utilisation pps Rx'], lmbda=0.5)


# dataframe['Utilisation pps Rx'], lam = boxcox(dataframe['Utilisation pps Rx'])
# print('Lambda: %f' % lam)
pyplot.figure(1)
# line plot
pyplot.subplot(211)
pyplot.plot(df['Utilisation pps Rx'])
# histogram
pyplot.subplot(212)
pyplot.hist(df['Utilisation pps Rx'])
pyplot.show()
