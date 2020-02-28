# https://scipy-cookbook.readthedocs.io/items/ButterworthBandpass.html
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html#scipy.signal.butter

# this script filters susashi.wav file and display the change
# information about susashi 1.5 Hz we are interested
# conversation frequency normal is under 15 Hz

# lowpass filter high cut to 15 Hz
# bandpass


import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

WAV_PATH = "susashi.wav"
print("******************************************************")
print("wav file loading from: " + WAV_PATH)
WAV_RATE, WAV_DATA = wav.read("susashi.wav")
print("wav file info:")
print("rate: " + str(WAV_RATE))
print("data: " + str(WAV_DATA))
print("data shape: " + str(WAV_DATA.shape))
print("******************************************************")

