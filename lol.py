import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

y=10

def blink():
  for x in range (0,y):
    GPIO.output(7,True)
    print "I am blinking -",x,"out of",y
    time.sleep(.5)
    GPIO.output(7,False)
    time.sleep(.5)
  print "I am OFF"
  
def onforten():
  GPIO.output(7,True)
  print "I am on for 10 seconds"
  time.sleep(10)
  GPIO.output(7,False)
  print "I am OFF"

blink()
onforten()
#skrivet = input ("Skriv et tal: ")

#for x in range (0,1):
#  if skrivet == 1:
#    print x+1
#    ost()
#  else:
#    print "skriv 1"

GPIO.cleanup()

print "Test is complete."
