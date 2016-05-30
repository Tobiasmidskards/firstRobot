import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.OUT)

p = GPIO.PWM(40, 10)

print "starting motor"
p.start(10)

time.sleep(5)

print "p.ChangeDutyCycle(90)"
p.ChangeDutyCycle(50)

time.sleep(5)

print "p.ChangeFrequency(100)"
p.ChangeFrequency(100)

time.sleep(5)

p.stop()

GPIO.cleanup()
