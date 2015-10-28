#!/usr/bin/python3
import pyaudio
import audioop
import wave

CHUNK = 256
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
THRESHOLD = 2000

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
	dev = p.get_device_info_by_index(i)
	print((i, dev['name'],dev['maxInputChannels']))

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
		input_device_index = 2,
                frames_per_buffer=CHUNK)

print("* recording")

while True:
    try:
    	data = stream.read(CHUNK)
    except IOError as ex:
	stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index = 2,
                frames_per_buffer=CHUNK)
	
	data = stream.read(CHUNK)
	
    rms = audioop.rms(data, 2)
    print(rms)
    if(rms>THRESHOLD):
    	break

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

