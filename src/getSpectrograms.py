from spectrograms import *

TMN_spect, TMN_freq = getSpectrogram(TMNframes)
TMF_spect, TMF_freq = getSpectrogram(TMFframes)
TMN_trans = np.transpose(TMN_spect)
TMF_trans = np.transpose(TMF_spect)

TMF_ave = prumerCharakteristiky(TMF_freq)
TMN_ave = prumerCharakteristiky(TMN_freq)

H = TMN_ave/TMF_ave # B(x) / A(x) = H(x)