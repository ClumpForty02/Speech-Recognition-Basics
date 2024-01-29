import wave
import numpy as np
import matplotlib.pyplot as plt

obj= wave.open("Recording.wav", "rb")

sample_freq= obj.getframerate()
sample_num= obj.getnframes()
signal_wave= obj.readframes(-1)
# print(type(obj.readframes(-1)))
obj.close()

t_audio= (sample_num/sample_freq)
print(t_audio)

signal_array= np.frombuffer(signal_wave, dtype=np.int16)
times= np.linspace(0, t_audio, num= sample_num)
signal_array = signal_array[:len(times)]

plt.figure(figsize=(15,5))
plt.plot(times, signal_array)
plt.ylabel("Signal wave")
plt.xlabel("Time")
plt.xlim(0, t_audio)
plt.show()
