import scipy.io as sio
import scipy.io.wavfile

a = sio.loadmat("matfile.mat")
print(a)
a = sio.whosmat("matfile.mat")
print(a)

RATE = 0
DATA = 0

# what is general properties of .mat file
# Rate and Data

sio.wavfile.write("matfile.wav", RATE, DATA)


