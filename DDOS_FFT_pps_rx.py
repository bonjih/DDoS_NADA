import numpy as np
import scipy as sp
import scipy.fftpack
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from hurst import compute_Hc

df = pd.read_csv('data/test_pps_rx_DDOS_epoch.csv', usecols=['Date', 'Utilisation pps Rx'], na_values=(0),
                 parse_dates=['Date'])

series = pd.Series(df['Utilisation pps Rx'])

# Evaluate Hurst equation
# H = 0.5 — Brownian motion
# 0.5 < H < 1.0 — persistent behavior
# 0 < H < 0.5 — anti-persistent behavior

H, c, data = compute_Hc(series, kind='change', simplified=True)
# H=0.8438, c=3.7466

f, ax = plt.subplots()
ax.plot(data[0], c * data[0] ** H, color="deepskyblue")
ax.scatter(data[0], data[1], color="purple")
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Time interval')
ax.set_ylabel('R/S ratio')
ax.grid(True)

print("H={:.4f}, c={:.4f}".format(H, c))

df['Date'] = pd.to_datetime(df.Date, unit='s')
df.set_index('Date', inplace=True)
df_sum = df.dropna()
date = pd.to_datetime(df.index)
df = (df_sum['Utilisation pps Rx'])

# N = len(df)

# fig, ax = plt.subplots(1, 1, figsize=(6, 3))
# df.plot(ax=ax, lw=.5)
# ax.set_xlabel('Date')
# ax.set_ylabel('Utilisation pps Rx')

# exaggerate the peak, makes it easier to find the most prevalent frequencies
top = np.max(df)
bottom = np.min(df)
mid = np.average(df)
normSamples = (df - mid)
normSamples /= top - bottom

# normaise pps rx
df = series.values
values = df.reshape((len(df), 1))
scaler = MinMaxScaler(feature_range=(0, 1))
scaler = scaler.fit(values)
normalized = scaler.transform(values)

# get PSD
pps_fft = sp.fftpack.fft(normalized)
pps_psd = np.abs(pps_fft) ** 2  # square absolute value get the PSD
fftfreq = sp.fftpack.fftfreq(len(pps_psd), 1 / 10)  # original unit is a month

# Find the peak frequency, only the positive frequencies
i = np.where(fftfreq > 0)
freqs = fftfreq[i]
peak_freq = freqs[pps_psd[i].argmax()]

# An inner plot to show the peak frequency
axes = plt.axes([0.55, 0.3, 0.3, 0.5])
plt.title('Peak frequency (DDoS)')
plt.plot(freqs[:8], pps_psd[:8])
plt.setp(axes, yticks=[])

# lot the power spectral density
fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.plot(fftfreq[i], 10 * np.log10(pps_psd[i]))
ax.set_xlabel('Frequency Bins (2 days)')
ax.set_ylabel('PSD (dB)')
#
# # Remove all the high frequencies and transform back from frequencies to signal
high_freq_fft = pps_fft.copy()
high_freq_fft[np.abs(fftfreq) > peak_freq] = 0
filtered_sig = sp.fftpack.ifft(high_freq_fft)
# filtered_sig = np.real(sp.fftpack.ifft(pps_fft_bis))

# fig, ax = plt.subplots(1, 1, figsize=(18, 6))
# df.plot(ax=ax, lw=.5)
# ax.plot_date(date, filtered_sig, '-')
# ax.set_ylim(0, 50000)
# ax.set_xlabel('Date')
# ax.set_ylabel('Utilisation pps Rx')
# plt.legend(['Original Sig', 'Filtered Sig'])
plt.show()
