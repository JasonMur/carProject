import tacho
import lcd
import time

lcd.lcd_init()
tacho.setGpioPin(2)
duration = 2
gateTime = 0.0001
cylinders = 4

while True:
	revs, dwellAngle = tacho.countPulses(cylinders, duration, gateTime)
	rpm = revs *60/duration
	lcdString = "RPM:" + str(rpm) 
	lcd.lcd_string(lcdString,0x80,1)
	lcdString = "Dwell Angle:" + str(dwellAngle)
	lcd.lcd_string(lcdString,0xC0,1)
	
	time.sleep(1)
