
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

        A = sums2
        x = np.log2(np.arange(1,len(A)))

        huber = HuberRegressor().fit(x[:,None], -np.ravel(A[1:,None]))
        slope = huber.coef_

    if plot == True:
        plt.scatter(x,y,s=5,color='red')
        plt.plot([min(x),max(x)],\
                 [min(x)*slope+yInt,max(x)*slope+yInt],color='black')

        print('The slope is:{0}'.format(slope))

    return slope
