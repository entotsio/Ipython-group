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


def myfft(t, y, flag):
    N = int(t.size)
    fs = 1/(t[2]-t[1])
    Y = np.fft.fft(y)[0:int(N/2)]
    freq = np.fft.fftfreq(N, 1/fs)[0:int(N/2)]
    if flag:
        plt.figure(2)
        plt.clf()
        # plt.xkcd()
        plt.subplot(211)
        plt.loglog(freq, np.abs(Y/N*2), label='fft of line')
        plt.ylabel('fft')
        # plt.legend(handles = [p2, p3])
        # plt.ylim((0.1,10))
        plt.ylim((0.00001, 10))
        plt.legend()
        plt.subplot(212)
        plt.semilogx(freq, np.angle(Y/N*2), label='angle')
        plt.xlabel('freq, Hz')
        plt.legend()
    return freq, Y

def helloname(name):
    print("Hello {}".format(name))