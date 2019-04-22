
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

def loglog(sums2,interval=None,type=None,plot=False,smoothing=None):

    if type is None:

        y = [np.log(item) for item in sums2]
        x = [1/(vel+1) for vel in interval]
        slope,yInt,_,_,_ = stats.linregress(x,y)

    elif type is 'Density':

        y = sums2
        x = [_ for _ in range(0,len(sums2))]

        if smoothing:
            ## Addition of smoothing for spanish moss
            pass

        slope,yInt,_,_,_ = stats.linregress(x, y)

    if plot == True:
        plt.scatter(x,y,s=5,color='red')
        plt.plot([min(x),max(x)],\
                 [min(x)*slope+yInt,max(x)*slope+yInt],color='black')

        print('The slope is:{0}'.format(slope))

    return slope
