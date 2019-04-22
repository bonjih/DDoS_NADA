import pandas as pd
from matplotlib import pyplot
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import kurtosis, skew, gmean, tstd
import numpy as np

df = pd.read_csv('data/test_pps_rx_DDOS_epoch.csv', usecols=['Utilisation pps Rx'])
# df = pd.read_csv('data/test_pps_rx_1_month_epoch.csv', usecols=['Utilisation pps Rx'])

print('gMean :', gmean(df))
print('tStd :', tstd(df))
print('Skew :', skew(df))
print('kurtosis :', kurtosis(df))
print('variance :', np.var(df))

# Normailse for hist
series = pd.Series(df['Utilisation pps Rx'])
df = series.values
values = df.reshape((len(df), 1))
scaler = MinMaxScaler(feature_range=(0, 1))
scaler = scaler.fit(values)
normalised = scaler.transform(values)

# histogram
pyplot.hist(normalised)
pyplot.show()
