
from Complexity.tools import plot
from scipy import signal
from scipy.fftpack import fft, fftshift

import math
import numpy as np

def spectral(X, numPoints=2**13):

    window = signal.hamming(numPoints)
    fftTrans = [sig*win for sig,win in zip(X,window)]

    A = fft(fftTrans)
    A = abs(A)
    A = A[0:int(len(A)/2)]
    A = 2*A[1:-1]
    A = A**2
    A = np.log2(A)

    slope = plot.loglog(A, type='Density', plot=False)

    return slope
