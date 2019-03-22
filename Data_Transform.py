
from pandas import Series
from pandas import DataFrame
# from numpy import sqrt
from numpy import log
from matplotlib import pyplot

series = Series.from_csv('data/test_pps_rx.csv', header=0)
dataframe = DataFrame(series.values)
dataframe.columns = ['Utilisation pps Rx']
# dataframe['Utilisation pps Rx'] = sqrt(dataframe['Utilisation pps Rx'])
dataframe['Utilisation pps Rx'] = log(dataframe['Utilisation pps Rx'] + 1) #add '+1' to deal with zero or neg values

pyplot.figure(1)

# line plot
pyplot.subplot(211)
pyplot.plot(dataframe['Utilisation pps Rx'])

# histogram
pyplot.subplot(212)
pyplot.hist(dataframe['Utilisation pps Rx'])
pyplot.show()
