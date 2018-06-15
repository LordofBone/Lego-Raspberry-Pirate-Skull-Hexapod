# imports
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
waitTime = 0.6

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

#leg positioning-C functions (unused)

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

# the left and right walk functions alternate by lifting the middle leg so the other 2 are off the ground, moving them back
# and then lowering the middle leg down, and moving the other 2 legs back to push the bot forward, then raising the middle leg again	
def leftWalk():

	raiseRight()
	
	setRightPositionA()
		
	lowerRight()
		
	setRightPositionB()
	
	raiseRight()
		
def rightWalk():

	raiseLeft()
	
	setLeftPositionB()
	
	lowerLeft()
	
	setLeftPositionA()
	
	raiseLeft()

def walkForward():
	# begin walk loop
	while True:

		leftWalk()
		
		rightWalk()
		# checks distance and if under a certain value with choose randomly to turn left or right
		if checkDistance() < 500:
			if random.randint(1, 100) < 50:
				turnLeft()
			else:
				turnRight()
	
def turnLeft():
	# begin left walk
	while True:

		leftWalk()
		# check distance again, if the minimum distance threshold is exceeded then proceed to walk forward again
		if checkDistance() > 500:
			walkForward()
		else:
			continue

def turnRight():
	# begin left walk
	while True:

		rightWalk()
		# check distance again, if the minimum distance threshold is exceeded then proceed to walk forward again
		if checkDistance() > 500:
			walkForward()
		else:
			continue


# getPositions()

# check distance, if the minimum distance threshold is exceeded then proceed to walk forward, if not choose randomly to turn left or right
if checkDistance() < 500:
	if random.randint(1, 100) < 50:
		turnLeft()
	else:
		turnRight()
else:
	walkForward()
