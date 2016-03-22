# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 12:57:46 2016

@author: en1m12
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1024;
tmin = 0;
tmax = 10;
t = np.linspace(tmin,tmax,N)
frq = 10
sig = np.sin(2*np.pi*frq*t)

fsig = np.fft.fft(sig)[0:N/2]
fsig = 2*fsig/N
f = np.fft.fftfreq(N, (tmax-tmin)/N)[0:N/2]

plt.close('all')
fig1 = plt.plot(f,abs(fsig))

plt.figure()
fig2 = plt.loglog(f,abs(fsig),label='FFT')
fig2 = plt.loglog(f,2*abs(fsig),label='FFT2')
plt.xlim([1,100])
plt.ylim([1e-4,3])
plt.legend()
#plt.xlabel()
#plt.xlabel('frequency, Hz')
#plt.legend(handles=fig2)

plt.figure()
fig3 = plt.subplot(212)
plt.subplot(211).loglog(f,abs(fsig),label='FFT')
plt.xlim([1,100])
plt.ylim([1e-4,3])
plt.subplot(212).semilogx(f,np.angle(fsig),label='FFT')
plt.xlim([1,100])
