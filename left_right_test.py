import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

for x in range (0,1):
	print "Turning left"
	GPIO.output(7,True)
	GPIO.output(13,True)
	time.sleep(1)
	GPIO.output(7,False)
	GPIO.output(13,False)
	print "Left turn complete"
	time.sleep(2)
	
for x in range (0,1):
	print "Turning right"
	GPIO.output(11,True)
	GPIO.output(15,True)
	time.sleep(1)
	GPIO.output(11,False)
	GPIO.output(15,False)
	print "Right turn complete"
	time.sleep(2)
	
GPIO.cleanup()

print "Test is completeeee."
