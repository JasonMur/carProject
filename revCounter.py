import tacho
import lcd
import time

lcd.lcd_init()
tacho.setTachoPin(2)
tacho.setTdcPin(3)
tacho.setStrobePin(4)
duration = 5
gateTime = 0.0001
cylinders = 4

while True:
	revs, advanceAngle, dwellAngle = tacho.countPulses(cylinders, duration, gateTime)
	rpm = revs *60/duration
	lcdString = "RPM:" + str(rpm) 
	lcd.lcd_string(lcdString,0x80,2)
	lcdString = "DW:" + str(dwellAngle)[0:4] + " AD:" + str(advanceAngle)[0:4]
	lcd.lcd_string(lcdString,0xC0,1)
	time.sleep(1)

