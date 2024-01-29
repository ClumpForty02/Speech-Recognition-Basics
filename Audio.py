import wave
import pyaudio

obj= wave.open("C:/Users/KIIT/Desktop/PycharmProjects/AudioPart/Recording.wav","rb")
print("Number of channels: ", obj.getnchannels())
print("Sample width: ", obj.getsampwidth())
print("Frame Rate: ", obj.getframerate())
print("Number of frames: ", obj.getnframes())
print("Parameters: ", obj.getparams())

time_audio= obj.getnchannels() / obj.getframerate()
print(time_audio)

frames= obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))
obj.close()

#Saving data- Writing

obj_new= wave.open("Recording_new.wav", "wb")
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(44100)
obj_new.close()

#Parameters
# -number of channels (2 independant- stereo)
# sample width
# frame rate/ sample frequency
# number of frames
# values of a frame



