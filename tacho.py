import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BCM)
tachoPin = 2
tdcPin = 3
strobePin = 4

def about():
	print("Tacho programme copyright Jason 2022")

def setTachoPin(newTachoPin):
	tachoPin = newTachoPin
	GPIO.setup(tachoPin, GPIO.IN)

def setTdcPin(newTdcPin):
        tdcPin = newTdcPin
        GPIO.setup(tdcPin, GPIO.IN)

def setStrobePin(newStrobePin):
        strobePin = newStrobePin
        GPIO.setup(strobePin, GPIO.OUT)

def countPulses(cylinders, duration, gateTime):
	loops = 0
	dwellCount = 0
	advanceCount = 0
	advanceLoops = 0
	revs = 0
	cylCount = 0
	cylinder = 0
	startTime = time.time()
	lastPointsSignal = 0
	lastTdcSignal = 0
	while  duration > (time.time()-startTime):
		pointsSignal = GPIO.input(tachoPin)
		if pointsSignal == 0: 
			dwellCount += 1
			if pointsSignal != lastPointsSignal:
				cylCount += 1
				advanceLoops = 0
				if cylinder == 1:
					GPIO.output(strobePin, True)
					cylinder = 3
				elif cylinder == 3:
					cylinder = 4
				elif cylinder == 4:
					cylinder = 2
				elif cylinder == 2:
					cylinder = 1
		else:
			GPIO.output(strobePin, False)
		lastPointsSignal = pointsSignal
		tdcSignal = GPIO.input(tdcPin)
		if tdcSignal == 0:
			cylinder = 3
			if tdcSignal != lastTdcSignal:
				advanceCount += advanceLoops
		lastTdcSignal = tdcSignal
		advanceLoops += 1
		loops += 1
		time.sleep(gateTime)
	GPIO.output(strobePin, False)
	revs = cylCount/cylinders
	advanceAngle = 360*advanceCount/(loops*2)
	dwellAngle = 360*dwellCount/(cylinders*loops)
	return revs, advanceAngle, dwellAngle


