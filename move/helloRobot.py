#!/usr/bin/python3
import ctypes
import api
import os
import time
import sys
import struct

def Main():
        command = 1
        #api.ServoShutdown()
        try:
                if api.Initialize():
                        print("Initalized")
                        command = 1
                else:
                        print("Intialization failed")
                #api.ServoShutdown()
                api.PlayAction(8)
                print('Stand up')
                #value = int(input("Turn head to"))
                #api.SetMotorValue(20, value)
                Run(command)
        except (KeyboardInterrupt):
                api.ServoShutdown()
                sys.exit()
        except():
                api.ServoShutdown()
                sys.exit()

def Run(command):
        if(command == 0):
               	api.PlayAction(8)
                print('Stand up')
                command = 1
        elif(command == 1):
                api.WalkMove(0)
                api.WalkTurn(20)
        elif(command == 2):
                api.WalkMove(0)
                api.WalkTurn(-20)
        Run(command)


if __name__ == "__main__": 
  Main()
