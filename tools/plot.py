
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

def loglog(sums2,interval=None,type=None,plot=False,smoothing=None):

    if type is None:

        y = [np.log(item) for item in sums2]
        x = [1/(vel+1) for vel in interval]
        slope, yInt, _,_,_ = stats.linregress(x,y)

    elif type is 'Density':
        from sklearn.linear_model import HuberRegressor

        y = -np.ravel(sums2[1:,None])
        x = np.log2(np.arange(1,len(y)+1))

        huber = HuberRegressor().fit(x[:,None], y)
        slope, yInt = huber.coef_, huber.intercept_

    if plot == True:
        plt.scatter(x,y,s=5,color='red')
        plt.plot([min(x),max(x)],\
                 [min(x)*slope+yInt,max(x)*slope+yInt],color='black')

        print('The slope is: {0}'.format(slope))

    return slope, yInt
