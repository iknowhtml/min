#!/usr/bin/python3
import sys

#appends api directory path to sys path
sys.path.append("/home/pi/HROS1-Framework/Linux/project/Human_Robots_Interaction_Fall15")
import api

import ctypes
import os
import time
import struct

#imports for audio
import pyaudio
import audioop
import wave

#constants for audio detection
CHUNK = 256
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
RECORD_SECONDS = 5
THRESHOLD = 2000


def Main():
	initialize()

	while True:
		detectSound()
		wave()

def initialize():
        try:
                if api.Initialize():
                        print("Initalized")
                else:
                        print("Intialization failed")
        except (KeyboardInterrupt):
                api.ServoShutdown()
                sys.exit()
        except():
                api.ServoShutdown()
                sys.exit()

def wave():
	api.PlayAction(25)
        print('Min Waved!')

def detectSound():
	#initialize sound pyaudio
        p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index = 2)
	
	print("detecting sound...")

	while True:
    		try:
        		data = stream.read(CHUNK)
    		except IOError as ex:
        		stream = p.open(format=FORMAT,
                	channels=CHANNELS,
                	rate=RATE,
                	input=True,
                	input_device_index = 2)

        		data = stream.read(CHUNK)

    		rms = audioop.rms(data, 2)
    		print(rms)
    		if(rms>THRESHOLD):
			print("*sound detected!")

			stream.stop_stream()
			stream.close()
			p.terminate()
			
			break

if __name__ == "__main__": 
  Main()
