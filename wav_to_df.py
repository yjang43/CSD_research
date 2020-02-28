import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

rate, data = wav.read("susashi.wav")
print(rate)
print(type(data))

def sixty_fps(rate, data:np.ndarray):
     def average(data, index, extract_count):
          sum = 0
          for i in range(extract_count):
               sum += data[index - i]
          return sum / extract_count

     extract_count = int(rate / 1000)
     extracted_list = list()
     index = extract_count
     while index < data.__len__():
          bit = data[index]
          # bit = average(data, index, extract_count)
          extracted_list.append(bit)
          index += extract_count
     ret = np.array(extracted_list)
     return ret

a = sixty_fps(rate, data)
wav.write("susashi_60.wav", 1000, a)

plt.plot(data)
plt.show()
