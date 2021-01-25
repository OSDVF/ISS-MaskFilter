from getFrequencies import *

def getSpectrogram(corrCoeficients):
    spectrs = []
    freqs = np.empty([100,1024], dtype=np.complex_)
    for i, corr in enumerate(corrCoeficients):
        paddedFFT = np.fft.fft(np.pad(corr,(0,1024 - len(corr))))
        spectrs.append(20*np.log10((np.abs(paddedFFT[0:512]))))
        freqs[i] = paddedFFT
    return spectrs, freqs

def prumerCharakteristiky(source):
    N = len(source[0])
    averageArray = np.empty(N)
    for i in range(N):
        average = 0
        for sample in source:
            average += np.abs(sample[i])
        average /= len(source)

        averageArray[i] = average
    return averageArray