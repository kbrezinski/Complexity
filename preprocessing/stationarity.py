
from statsmodels.tsa.stattools import adfuller,kpss
import warnings

def fuller_test(interval,y):
    ## Diadic: 2 or Triadic: 3 shopping
    cond = False

    result = adfuller(y)

    if result[4]['5%'] > result[0]:
        print('Stationary interval found at frame size equal to epoch')
        cond = True
        frame = y

    while True and cond == False:
        init = 0
        interFrame = round(len(y)/interval)

        if interFrame < 64:
            print('ERROR: Frame size is less than 64 points')
            break

        frame = []

        while init < len(y):
            result = adfuller(y[init:interFrame+init])

            if result[4]['5%'] < result[0]:
                break

            elif init+interFrame == len(y):
                print('Stationary interval found at frame size: {0}, total number of frames: {1}'\
                    .format(interFrame, len(y)/interFrame))
                frame.append(y[init:interFrame+init])
                cond = True
                break

            frame.append(y[init:interFrame+init])

            init += interFrame

        if cond:
            break

        interval *= 2

    return frame

def kpss_test(interval,y):
    warnings.filterwarnings("ignore")
    ## Diadic: 2 or Triadic: 3 shopping
    cond = False

    result = kpss(y)

    if result[3]['5%'] > result[0]:
        print('Stationary interval found at frame size equal to epoch')
        cond = True
        frame = y

    while True and cond == False:
        init = 0
        interFrame = round(len(y)/interval)

        if interFrame < 64:
            print('ERROR: Frame size is less than 64 points')
            break

        frame = []

        while init < len(y):
            result = kpss(y[init:interFrame+init])

            if result[3]['5%'] < result[0]:
                break

            elif init+interFrame == len(y):
                print('Stationary interval found at frame size: {0}, total number of frames: {1}'\
                    .format(interFrame, len(y)/interFrame))
                frame.append(y[init:interFrame+init])
                cond = True
                break

            frame.append(y[init:interFrame+init])

            init += interFrame

        if cond:
            break

        interval *= 2

    return frame

def determine_interval(intervals,df,labels):
    """
    @Author: Kenneth Brezinski, Department of Electrical and Computer Engineering

    args:
        df: pandas dataframe containing your time series
        intervals: how many subintervals will be returned
        labels: a (2,1) list containing the strings of your two dataframe columns, e.g. ['Time','Bits']
        sensitivity: depending on the sensitivity of your distribution, may need to adjust to find indices

    return:
        appLists: a list of lists containing your dataframe separated into intervals

    """

    appLists = []

    init = 0
    stopCond = max(df[labels[0]])/intervals
    sensitivity = 1E-9
    dfb = []

    while len(dfb) != intervals-1:
        print(len(dfb))
        dfb = df[df[labels[0]] % stopCond < sensitivity].index
        sensitivity *= 10

    for item in dfb[1:]:
        appLists.append(df[labels[1]][init:item])
        init = item

    return appLists

def determine_intervalV2(frameSize, y, overlap=None, percent=None):

    init = 0
    frames = []

    if not overlap:
        for element in range(frameSize,len(y),frameSize):
            frames.append(y[init:element])
            init = element

    else:
        lap = frameSize-round(frameSize*percent)

        for element in range(frameSize,len(y),lap):
            frames.append(y[init:element])
            init += lap

    return frames
