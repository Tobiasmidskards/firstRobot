import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

GPIO.output(18,True)
GPIO.output(40,True)
time.sleep(5)
GPIO.output(18,False)
GPIO.output(40,False)

GPIO.cleanup()
