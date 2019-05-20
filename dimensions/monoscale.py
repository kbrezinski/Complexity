
import numpy as np

def zero_cross(y):

    mn = np.mean(y) #Set the mean of the signal
    count = 0    #Set the number of crosses to 0
    last = y[0] - mn  #Set the last index to first index

    for elem in range(len(y)):
        diff = y[elem] - mn

        # If subsequent steps change sign, i.e. cross over the mean
        # add 1 to the counter
        if np.sign(diff) != np.sign(last):
            count += 1
        last = diff

    return count

def turn_count(y, smooth=False, smooth_params=[111,10]):

    import scipy as sp
    count = 0; last = 0

    if smooth:
        y = sp.signal.savgol_filter(y , smooth_params[0], 1)

    for elem in range(0, len(y)-smooth_params[1], smooth_params[1]):
        diff = y[elem] - y[elem + smooth_params[1]]
        if np.sign(diff) != np.sign(last):
            count += 1
        last = diff

    return count - 1
