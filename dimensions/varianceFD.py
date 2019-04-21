
import statistics as stat
import numpy as np

def variance(result, interval):

    from Complexity.preprocessing import intervals

    result = intervals.subinterval(result, interval, type='Length')

    result2 = []; sums = []

    for item in result:
        newArray = np.asarray(item)
        result2.append((1/(newArray.shape[0]-1))*sum((newArray - sum(newArray)/newArray.shape[0])**2).tolist())

    idx1 = 1
    for inter in interval:
        if inter == 0:
            sums.append(result2[0])
        else:
            sums.append(sum([result2[i] for i in range(idx1,(idx1+inter+1))])/(inter+1))
            idx1 += inter+1

    DL = plot.loglog(sums3,interval,plot=False)

    return DL
