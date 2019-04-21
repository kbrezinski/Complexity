
import numpy as np

def subinterval(y, interval, type=None):

    result = []

    if type == None:

        for inter in interval:
            for init in interval:
                res = []
                if inter >= init:
                    for i in range(init,len(y)-inter-1,inter+1):
                        res.append(y[i])
                    result.append(res)

    elif type == 'length':

        for inter in interval:
            for init in interval:
                res = []
                if inter >= init:
                    for i in range(init,len(y)-inter-1,inter+1):
                        res.append(abs(y[i+inter+1]-y[i]))
                    result.append(res)

    elif type == 'variance':
        pass

    else:
        pass

    return result

def intervalSums(result,interval, type=None):
    ## Concatenate and Sum
    sums = []; sums2 = []
    idx1 = 0

    if type == None:

        for inter in interval:
            if inter == 0:
                sums.append(sum(result[0]))
            else:
                sums.append(sum([sum(result[i]) for i in range(idx1,(idx1+inter+1))])/(inter+1))
                idx1 += inter+1

        def removeNestings(a):
            for i in a:
                if type(i) == np.ndarray:
                    removeNestings(i)
                else:
                    sums2.append(i)

            return sums2

        sums2 = removeNestings(sums)

    if type == 'variance':

        for inter in interval:
                sums2.append(sum([result[i] for i in range(idx1,(idx1+inter+1))])/(inter+1))
                idx1 += inter+1

    return sums2
