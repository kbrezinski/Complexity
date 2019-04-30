
import statistics as stat
import numpy as np

from Complexity.preprocessing import intervals
from Complexity.tools import plot

def length(result, interval):

    # Some of these may be redundant
    sums3 = []

    result = intervals.subinterval(result, interval, type='length')

    for inter in interval:
        idx1 = 0
        if inter == 0:
            sums3.append(sum(result[0]))
        else:
            sums3.append(sum([sum(result[i]) for i in range(idx1,(idx1+inter+1))])/(inter+1))
            idx1 += inter+1

    slope = plot.loglog(sums3,interval,plot=False)

    DL = 1 + slope

    return DL
