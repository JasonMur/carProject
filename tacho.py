import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BCM)
gpioPin = 2

def about():
	print("Tacho programme copyright Jason Industries 2022")

def setGpioPin(newGpioPin):
	gpioPin = newGpioPin
	GPIO.setup(gpioPin, GPIO.IN)

def countPulses(cylinders, duration, gateTime):
	loops = 0
	dwellCount = 0
	revs = 0
	cylCount = 0
	startTime = time.time()
	lastPointsSignal = 0
	while  duration > (time.time()-startTime):
		pointsSignal = GPIO.input(gpioPin)
		if pointsSignal == 0: 
			dwellCount += 1
		else:
			if pointsSignal != lastPointsSignal:
				cylCount += 1
		lastPointsSignal = pointsSignal
		loops += 1
		time.sleep(gateTime)
	revs = cylCount/cylinders
	dwellAngle = 360*dwellCount/(cylinders*loops)
	return revs, dwellAngle
