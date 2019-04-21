
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

def loglog(sums2,interval,plot=True):

    y = [np.log(item) for item in sums2]
    x = [1/(vel+1) for vel in interval]
    slope,yInt,_,_,_ = stats.linregress(x,y)

    if plot == True:
        plt.scatter(x,y)
        plt.plot([min(x),max(x)],[min(x)*slope+yInt,max(x)*slope+yInt])

        print('The slope is:{0}'.format(slope))

    return slope
