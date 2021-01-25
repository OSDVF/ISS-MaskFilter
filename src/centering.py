from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [8, 5]

fs, tmf = wavfile.read('../audio/maskoff_tone.wav')
fs, tmn = wavfile.read('../audio/maskon_tone.wav')

def extractOneSecond(fromSamples,toSamples,source):
    center = (source - np.mean(source))[int(fromSamples):int(toSamples+1)]
    center /= np.abs(center).max()
    mn = center.min()
    mx = center.max()
    print("Normalizovaný rozsah: ", mn, mx)
    return center, mn, mx

TMFcent, TMFmin, TMFmax = extractOneSecond(16000, 16000*2.01, tmf)
TMNcent, TMNmin, TMNmax = extractOneSecond(16000*1.6, 16000*2.61, tmn)

#TMFcent, TMFmin, TMFmax = extractOneSecond(0, 16000*1.01, tmf)
#TMNcent, TMNmin, TMNmax = extractOneSecond(0, 16000*1.01, tmn)

#TMFcent, TMFmin, TMFmax = extractOneSecond(16000*1.2, 16000*2.21, tmf)
#TMNcent, TMNmin, TMNmax = extractOneSecond(16000*2.5, 16000*3.51, tmn)