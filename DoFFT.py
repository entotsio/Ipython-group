# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 12:57:44 2016

@author: gs13g11
"""

import numpy as np
import matplotlib.pyplot as plt
# %matplotlib qt
# %matplotlib inline
# %reset -f
# %reset

plt.close('all')

T = 10
fs = 1024
f0 = 1000

t = np.linspace(0, T, fs*T)
N = t.size
y = np.sin(2*np.pi*f0*t)

plt.figure(1)
plt.clf()
p1 = plt.plot(t, y, label='line')
plt.legend(handles=p1)

Y = np.fft.fft(y)[0:int(N/2)]
df = 1/T
freq = np.fft.fftfreq(N, 1/fs)[0:int(N/2)]
plt.figure(2)
plt.clf()
# plt.xkcd()
plt.subplot(211)
plt.loglog(freq, np.abs(Y/N*2), label='fft of line')
plt.loglog(freq, np.abs(Y/N*2)*10, label='10 * fft of line')
plt.ylabel('fft')
# plt.legend(handles = [p2, p3])
# plt.ylim((0.1,10))
plt.ylim((0.00001, 10))
plt.legend()
plt.subplot(212)
plt.semilogx(freq, np.angle(Y/N*2), label='angle')
plt.xlabel('freq, Hz')
plt.legend()

# %%
np.save('savedY.npy', Y)
np.savez('savedYf', Y=Y, freq=freq)
# %%
Y = np.load('savedY.npy')
data = np.load('savedYf.npz')
data.files
Y = data['Y']
freq = data['freq']
