import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

for x in range (0,10):
  GPIO.output(7,True)
  print "Motor 1-7 is running"
  time.sleep(0.1)
  
GPIO.cleanup()

print "Test is complete."
