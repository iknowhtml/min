#!/usr/bin/python3
import sys

#appends api directory path to sys path
sys.path.append("/home/pi/HROS1-Framework/Linux/project/Human_Robots_Interaction_Fall15")
import api

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

def Main():
    initialize()
    while True:
        detectFace() 

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


if __name__ == "__main__": 
  Main()
