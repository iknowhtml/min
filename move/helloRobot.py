#!/usr/bin/python3
import sys

sys.path.append("/home/pi/HROS1-Framework/Linux/project/Human_Robots_Interaction_Fall15")
import api

import ctypes
import os
import time
import struct

def Main():
        #api.ServoShutdown()
        try:
                if api.Initialize():
                        print("Initalized")
                else:
                        print("Intialization failed")
                Run()
        except (KeyboardInterrupt):
                api.ServoShutdown()
                sys.exit()
        except():
                api.ServoShutdown()
                sys.exit()

def Run():
        #api.Walk(True)
        #print("Running...")
        #move foward
                api.PlayAction(8)
                print('Stand up')
                api.WalkMove(0)
                api.WalkTurn(20)
		print('Walk in circle')
		api.PlayAction(25)
                print('Wave')


if __name__ == "__main__": 
  Main()
