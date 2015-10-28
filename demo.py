#!/usr/bin/python3
import sys

#appends api directory path to sys path
sys.path.append("/home/pi/HROS1-Framework/Linux/project/Human_Robots_Interaction_Fall15")

import ctypes
import os
import time
import struct

#import opencv
import cv2

#sets up face cascade
cascPath = 'face_cascade.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(-1)

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

    while True:
        detectFace()
        
        import api
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
        
        api.PlayAction(8)
        print("Min Stood up!")

        detectSound()
        
        api.PlayAction(15)
        print("Min Sat Down!")

        api.PlayAction(25)
        print('Min Waved!')

def detectFace():
    val = 0

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        if val % 10 == 0:   
            print("analyzing frame")
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
        
            print("frame analyzed!")
            #Draw a rectangle around the faces
            
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            if len(faces):
                print("face detected")
                # When everything is done, release the capture
                #video_capture.release()
                cv2.destroyAllWindows()
                break
            
            # Display the resulting frame
            cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        val+= 1

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

        if(rms > THRESHOLD):
		  print("*sound detected!")

		  stream.stop_stream()
		  stream.close()
		  p.terminate()
		
		  break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__": 
  Main()
