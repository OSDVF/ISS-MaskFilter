from clip import *

Fs = 16000.0
minLag = int(Fs/500.0)
def allBaseFreqs(source, frameSize):
    correlations = []
    baseFrequencies = []
    frames = np.empty([100, frameSize])
    for i in range(0,100): #for every rámec
        frameStart = int(i*(frameSize/2))
        frameEnd = frameStart + frameSize
        frames[i] = source[frameStart:frameEnd]
        correlations.append(centralClipping(frames[i]))
        correlations[i], baseFr = computeBaseFrequency(correlations[i], frameSize, Fs, minLag)
        baseFrequencies.append(baseFr)
    return frames, correlations, baseFrequencies

TMFframes, TMFcorr, TMFfreqs = allBaseFreqs(TMFcent, frameSize)
TMNframes, TMNcorr, TMNfreqs = allBaseFreqs(TMNcent, frameSize)

print("minLag: ", minLag)

maxIndex = np.argmax(TMFcorr[targetFrameIndex][minLag:frameSize]) + minLag

print("F0 = ", TMFfreqs[targetFrameIndex])
print("maxIndex = ", maxIndex)