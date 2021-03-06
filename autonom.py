import RPi.GPIO as GPIO
import time
from random import randint as rints

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT) # LED WHITE
GPIO.setup(40, GPIO.OUT) # LED RED

GPIO.setup(7, GPIO.OUT)  # MOTOR 1-7
GPIO.setup(11,GPIO.OUT)  # MOTOR 2-11
GPIO.setup(13,GPIO.OUT)  # MOTOR 3-13
GPIO.setup(15,GPIO.OUT)  # MOTOR 4-15

GPIO.setup(12,GPIO.OUT)  # DISTANCE TRIGGER
GPIO.setup(16, GPIO.IN)  # DISTANCE ECHO

def forwardon():
	# Go forward
	print "Going forward"
	GPIO.output(11,True)
	GPIO.output(15,True)
	
def forwardoff():
	# Go forward
	print "Going forward is off"
	GPIO.output(11,False)
	GPIO.output(15,False)

def left():
	# Turn left
	print "Turning left"
	GPIO.output(7,True)
	GPIO.output(15,True)
	time.sleep(.8)
	GPIO.output(7,False)
	GPIO.output(15,False)

def right():
	# Turn right
	print "Turning right"
	GPIO.output(13,True)
	GPIO.output(11,True)
	time.sleep(.8)
	GPIO.output(13,False)
	GPIO.output(11,False)

def back():
	# Go backwards
	print "Going backwards"
	GPIO.output(7,True)
	GPIO.output(13,True)
	time.sleep(1)
	GPIO.output(7,False)
	GPIO.output(13,False)

def led():
	# Led blink
	print "Led blink 3 times"
	for b in range (0,3):
		GPIO.output(18,True)
		GPIO.output(40,True)
		time.sleep(0.5)
		GPIO.output(18,False)
		GPIO.output(40,False)
		time.sleep(0.5)
	
	# Led on permanently
	
	# Led off

def distance(measure='cm'):
		
		time.sleep(0.3)
		GPIO.output(12,True)
		time.sleep(0.00001)
		
		GPIO.output(12, False)
		while GPIO.input(16) == 0:
				nosig = time.time()
				
		while GPIO.input(16) == 1:
				sig = time.time()
				
		tl = sig - nosig
		
		distance = tl / 0.000058
				
		return distance
		
		

def main():
	# autonom main function
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(18, GPIO.OUT) # LED WHITE
		GPIO.setup(40, GPIO.OUT) # LED RED

		GPIO.setup(7, GPIO.OUT)  # MOTOR 1-7
		GPIO.setup(11,GPIO.OUT)  # MOTOR 2-11
		GPIO.setup(13,GPIO.OUT)  # MOTOR 3-13
		GPIO.setup(15,GPIO.OUT)  # MOTOR 4-15

		GPIO.setup(12,GPIO.OUT)  # DISTANCE TRIGGER
		GPIO.setup(16, GPIO.IN)  # DISTANCE ECHO
		
		distance()
		
		print distance()
		
		if distance() < 20:
			forwardoff()
			led()
			back()
			r = rints(0,1)
			if r == 1:
				left()
			else:
				right()
		else:
			forwardon()
			
		GPIO.cleanup()

for x in range (0,10):
	main()
