
import numpy as np
import scipy as sp
import scipy.fftpack
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/test_pps_rx_DDOS_epoch.csv', usecols=['Date', 'Utilisation pps Rx'], na_values=(0),
                 parse_dates=['Date'])

df['Date'] = pd.to_datetime(df.Date, unit='s')
df.set_index('Date',inplace=True)
df_sum = df.dropna()
date = pd.to_datetime(df.index)
df = (df_sum['Utilisation pps Rx'])

# N = len(df)

fig, ax = plt.subplots(1, 1, figsize=(6, 3))
df.plot(ax=ax, lw=.5)
ax.set_xlabel('Date')
ax.set_ylabel('Utilisation pps Rx')

pps_fft = sp.fftpack.fft(df)
pps_psd = np.abs(pps_fft) ** 2
fftfreq = sp.fftpack.fftfreq(len(pps_psd), 1 / 31) #original unit is a month

# Find the peak frequency, only the positive frequencies
i = np.where(fftfreq > 0)
freqs = fftfreq[i]
peak_freq = freqs[pps_psd [i].argmax()]

# An inner plot to show the peak frequency
axes = plt.axes([0.55, 0.3, 0.3, 0.5])
plt.title('Peak frequency')
plt.plot(freqs[:8], pps_psd[:8])
plt.setp(axes, yticks=[])

#lot the power spectral density
fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.plot(fftfreq[i], 10 * np.log10(pps_psd[i]))
ax.set_xlabel('Frequency (1/month)')
ax.set_ylabel('PSD (dB)')

# Remove all the high frequencies and transform back from frequencies to signal
high_freq_fft = pps_fft.copy()
high_freq_fft[np.abs(fftfreq) > peak_freq] = 0
filtered_sig = sp.fftpack.ifft(high_freq_fft)

# filtered_sig = np.real(sp.fftpack.ifft(pps_fft_bis))
fig, ax = plt.subplots(1, 1, figsize=(18, 6))
df.plot(ax=ax, lw=.5)
ax.plot_date(date, filtered_sig, '-')
ax.set_ylim(0, 50000)
ax.set_xlabel('Date')
ax.set_ylabel('Utilisation pps Rx')
plt.legend(['Original Sig', 'Filtered Sig'])
plt.show()
