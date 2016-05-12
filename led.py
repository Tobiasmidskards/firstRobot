import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

GPIO.output(18,True)
time.sleep(1)
GPIO.output(18,False)

GPIO.cleanup()
