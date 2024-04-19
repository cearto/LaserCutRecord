#this code unpacks and repacks data from:
#16 bit stereo wav file at 44100hz sampling rate
#to:
##16 bit mono wav file at 44100hz sampling rate

import wave
import math
import struct

bitDepth = 8#target bitDepth
frate = 44100#target frame rate
fileName = "heartbeatloop.wav"#file to be imported (change this)

#read file and get data
w = wave.open(fileName, 'r')
sample_width = w.getsampwidth()
channels = w.getnchannels()

print(f"FILE: {fileName}")
if channels == 1:
    print("This is a mono audio file.")
else:
    print("This is a stereo audio file.")

if sample_width == 1:
    print("This is an 8-bit audio file.")
elif sample_width == 2:
    print("This is a 16-bit audio file.")
else:
    print("This audio file has a different bit depth.")

numframes = w.getnframes()

frames = w.readframes(numframes)

#separate left and right channels and merge bytes
if channels == 1:
    left = [struct.unpack('<h', frames[i:i+2])[0] for i in range(0, len(frames), 2)]
if channels == 2:
    left = [struct.unpack('<h', frames[i:i+4])[0] for i in range(0, len(frames), 4)]
    right = [struct.unpack('<h', frames[i+2:i+4])[0] for i in range(0, len(frames), 4)]


# convert to string
audioStr = ','.join(map(str, left))

fileName = fileName[:-3]#remove .wav extension
text_file = open(fileName+"txt", "w")
text_file.write("%s"%audioStr)
text_file.close()



