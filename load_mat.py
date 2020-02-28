import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt

MAT_PATH = "matfile.mat"
mat_file = sio.loadmat(MAT_PATH)
mat_file_info = sio.whosmat(MAT_PATH)

print("******************************************************")

print("mat file loading from: " + MAT_PATH)
print("mat file info: ")
for section in mat_file_info:
    print(section)

print("******************************************************")

MAT_RATE = 8000                 # 8000 samples per second
MAT_DATA = mat_file['data']     # numpy each row su sa shi normal and inversion 450 rep
print("DATA loaded")
print("DATA shape: " + str(MAT_DATA.shape))

print("******************************************************")
# susashi needs to get an envelope for that
# susashi and EEG needs 15 Hz
# envelope below 15 Hz
# artifact rejection


# sio.wavfile.write("matfile.wav", RATE, DATA)


