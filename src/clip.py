from centering import *
import matplotlib.lines as mlines
frameSize = int((16000/100)*2)
targetFrameIndex = 1
targetStart = int(targetFrameIndex*(frameSize/2))
TMFfirst = TMFcent[targetStart:targetStart + frameSize].copy()

# Centrální klipování s prahem 60%
def centralClipping(source):
    output = np.empty(source.shape)
    positiveMax = np.max(np.abs(source)) * 0.6
    for i, sample in enumerate(source):
        if sample < - positiveMax:
            output[i] = -1
        elif sample > positiveMax:
            output[i] = 1
        else:
            output[i] = 0
    return output

def computeBaseFrequency(source, frameSize, Fs, minLag):
    #Correlation
    corr = []
    for m in range(0, frameSize):
        sum = 0.0
        for n in range(m,frameSize):
            sum += source[n] * source[n - m] 
        corr.append(sum)
    maxIndex = np.argmax(corr[minLag:frameSize]) + minLag
    f0 = Fs/maxIndex
    return corr, f0