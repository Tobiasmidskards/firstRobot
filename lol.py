import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

def ost():
  GPIO.output(7,True)
  time.sleep(1)
  GPIO.output(7,False)
  time.sleep(1)

skrivet = input "Vælg et tal: "

for x in range (0,10):
  print x+1
  if input = 1:
    ost()
  else:
    print "skriv 1"

GPIO.cleanup()

print "Test is complete."
