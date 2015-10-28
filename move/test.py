#!/usr/bin/python3
import sys, os, ctypes, time
import api

if api.Initialize():
    print("Initialized")
else:
    print("Initialization failed")
    sys.exit(1)

print("Battery voltage:", api.BatteryVoltLevel() / 10)

# print('Standing...')
# api.PlayAction(1)
# print('Finished standing')

# print('Motor 20 value:', api.GetMotorValue(20))
# api.SetMotorValue(20, 600)
# time.sleep(1)
# print('Motor 20 value set:', api.GetMotorValue(20))
# print('Motor 19 value:', api.GetMotorValue(19))
# api.SetMotorValue(19, 600)
# time.sleep(1)
# print('Motor 19 value set:', api.GetMotorValue(19))

value = int(input("Turn head to: "))
api.SetMotorValue(20, value)

# api.Walk(True)
# api.WalkMove(20)
# print('Walking...')
# time.sleep(3)

# api.WalkMove(0)
# api.WalkTurn(20)
# print('Turning...')
# time.sleep(3)

# api.Walk(False)
# print('Stopped walking')

api.ServoShutdown()
print('Finished')
