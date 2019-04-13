from pandas import Series
from pandas import DataFrame
from scipy.stats import boxcox
from matplotlib import pyplot


# lambda = -1. is a reciprocal transform.
# lambda = -0.5 is a reciprocal square root transform.
# lambda = 0.0 is a log transform.
# lambda = 0.5 is a square root transform.
# lambda = 1.0 is no transform

# dataset gives Lambda: 0.205324, need to work out if log or sqr is the best


series = Series.from_csv('data/test_pps_rx_1_month_epoch.csv', header=0)

dataframe = DataFrame(series.values)
dataframe.columns = ['Utilisation pps Rx']
dataframe['Utilisation pps Rx'] = boxcox(dataframe['Utilisation pps Rx'], lmbda=0.5)

# dataframe['Utilisation pps Rx'], lam = boxcox(dataframe['Utilisation pps Rx'])
# print('Lambda: %f' % lam)
pyplot.figure(1)
# line plot
pyplot.subplot(211)
pyplot.plot(dataframe['Utilisation pps Rx'])
# histogram
pyplot.subplot(212)
pyplot.hist(dataframe['Utilisation pps Rx'])
pyplot.show()
