# Setup the library ready for use
import UltraBorg
import sys
import time
import random

# ub1: left
# ub2: right
# 2: back
# 3: front
# 4: middle

# Board #1, address 10
UB1 = UltraBorg.UltraBorg()
UB1.i2cAddress = 10
UB1.Init()

# Board #2, address 11
UB2 = UltraBorg.UltraBorg()
UB2.i2cAddress = 11
UB2.Init()

# positionTest = float(sys.argv[1])
full = float(1.0)
zero = float(0)
waitTime = 0.7

# get positions function

def getPositions():

	print (UB1.GetServoPosition2())		# Read the current position of servo #2
	print (UB1.GetServoPosition3())		# Read the current position of servo #3
	print (UB1.GetServoPosition4())		# Read the current position of servo #4

	print (UB2.GetServoPosition2())		# Read the current position of servo #2
	print (UB2.GetServoPosition3())		# Read the current position of servo #3
	print (UB2.GetServoPosition4())		# Read the current position of servo #4

# leg positioning-A functions

def setRightPositionA():

	#right legs
	UB2.SetServoPosition2(full)		# Set the current position of servo #2
	UB2.SetServoPosition3(full)		# Set the current position of servo #3
	#UB2.SetServoPosition4(full)		# Set the current position of servo #4
	time.sleep(waitTime)

def setLeftPositionA():

	#left legs
	UB1.SetServoPosition2(full)		# Set the current position of servo #2
	UB1.SetServoPosition3(full)		# Set the current position of servo #3
	#UB1.SetServoPosition4(full)		# Set the current position of servo #4
	time.sleep(waitTime)

#leg postioning-B functions

def setRightPositionB():

	#right legs
	UB2.SetServoPosition2(zero)		# Set the current position of servo #2
	UB2.SetServoPosition3(zero)		# Set the current position of servo #3
	#UB2.SetServoPosition4(zero)		# Set the current position of servo #4
	time.sleep(waitTime)

def setLeftPositionB():

	#left legs
	UB1.SetServoPosition2(zero)		# Set the current position of servo #2
	UB1.SetServoPosition3(zero)		# Set the current position of servo #3
	#UB1.SetServoPosition4(zero)		# Set the current position of servo #4
	time.sleep(waitTime)

#leg positioning-C functions

def setRightPositionC():

	#right legs
	UB2.SetServoPosition2(full)		# Set the current position of servo #2
	UB2.SetServoPosition3(zero)		# Set the current position of servo #3
	UB2.SetServoPosition4(full)		# Set the current position of servo #4
	time.sleep(waitTime)

def setLeftPositionC():

	#left legs
	UB1.SetServoPosition2(zero)		# Set the current position of servo #2
	UB1.SetServoPosition3(full)	# Set the current position of servo #3
	UB1.SetServoPosition4(zero)	# Set the current position of servo #4
	time.sleep(waitTime)

def raiseLeft():
		
	#left legs
	UB1.SetServoPosition4(full)	# Set the current position of servo #3
	time.sleep(waitTime)
		
def raiseRight():

	#left legs
	UB2.SetServoPosition4(full)	# Set the current position of servo #3
	time.sleep(waitTime)
		
def lowerLeft():
		
	#left legs
	UB1.SetServoPosition4(zero)	# Set the current position of servo #3
	time.sleep(waitTime)
		
def lowerRight():

	#left legs
	UB2.SetServoPosition4(zero)	# Set the current position of servo #3
	time.sleep(waitTime)
		
def checkDistance():
	# checks distance using ultrasonics and returns the value
	time.sleep(waitTime)
	return UB1.GetDistance1()
	time.sleep(waitTime)
	
def leftWalk():

	lowerLeft()
	
	setLeftPositionA()
	
	raiseLeft()
	
	setLeftPositionB()
		
def rightWalk():

	raiseRight()
	
	setRightPositionA()
		
	lowerRight()
		
	setRightPositionB()

def walkForward():
	# begin walk loop
	while True:

		leftWalk()
		
		rightWalk()

		if checkDistance() < 300:
			if random.randint(1, 100) < 50:
				turnLeft()
			else:
				turnRight()
	
def turnLeft():
	# begin left walk
	while True:

		leftWalk()

		if checkDistance() > 300:
			walkForward()
		else:
			continue

def turnRight():
	# begin left walk
	while True:

		rightWalk()

		if checkDistance() > 300:
			walkForward()
		else:
			continue


# getPositions()

if checkDistance() < 300:
	if random.randint(1, 100) < 50:
		turnLeft()
	else:
		turnRight()
else:
	walkForward()
