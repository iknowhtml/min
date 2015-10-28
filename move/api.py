import os, ctypes
from ctypes import *

_API_DIR = '../Human_Robots_Interaction_Fall15'
os.chdir(_API_DIR)

_apiwrapper = CDLL(os.path.join(_API_DIR, 'apiwrapper.so'))

Initialize = _apiwrapper.InitializeJS #Initializes the robot. Without this function nothing will work.
Initialize.argtypes = []              # Make sure it returns true, otherwise it won't work
Initialize.restype = c_bool
ServoShutdown = _apiwrapper.ServoShutdownJS #Shutdown the servo, if you call it, you have to call Initialize to be  
ServoShutdown.argtypes = []                 #able to call other functions.(make sure robot is sitting before calling it)
ServoShutdown.restype = None
ServoStartup = _apiwrapper.ServoStartupJS   # Turn on servos- once called, all servos will be locked
ServoStartup.argtypes = []
ServoStartup.restype = None
PlayAction = _apiwrapper.PlayActionJS     #play action page - the argument is the RME page number
PlayAction.argtypes = [c_int]
PlayAction.restype = c_int
Walk = _apiwrapper.WalkJS             # Start walking if True, stop when False
Walk.argtypes = [c_bool]
Walk.restype = None
Walking = _apiwrapper.WalkingJS     #location walking- Walk to X,Y location
Walking.argtypes = [c_int, c_int]
Walking.restype = None
WalkMove = _apiwrapper.WalkMoveJS   #Walk forward if positive value, walk back if negative( the bigger the abs(value)
WalkMove.argtypes = [c_double]      # the faster it walks
WalkMove.restype = None
WalkTurn = _apiwrapper.WalkTurnJS   #Turn left if Negative, right if positive- the bigger the abs(value) the faster it turns
WalkTurn.argtypes = [c_double]
WalkTurn.restype = None
CheckServos = _apiwrapper.CheckServosJS #check if servo is working- return true or false
CheckServos.argtypes = []
CheckServos.restype = c_int
BatteryVoltLevel = _apiwrapper.BatteryVoltLevelJS  #check batter level
BatteryVoltLevel.argtypes = []
BatteryVoltLevel.restype = c_int
SetMotorValue = _apiwrapper.SetMotorValueJS     #set a servo value, aguments:(servo ID(1-20), Servo Value(0-1024))
SetMotorValue.argtypes = [c_int, c_int]
SetMotorValue.restype = None
GetMotorValue = _apiwrapper.GetMotorValueJS     #get a servo value, argument (servo id(1-20)
GetMotorValue.argtypes = [c_int]
GetMotorValue.restype = c_int
