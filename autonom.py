import RPi.GPIO as GPIO
import time
from random import randint as rints

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT) # LED

GPIO.setup(7, GPIO.OUT)  # MOTOR 1-7
GPIO.setup(11,GPIO.OUT)  # MOTOR 2-11
GPIO.setup(13,GPIO.OUT)  # MOTOR 3-13
GPIO.setup(15,GPIO.OUT)  # MOTOR 4-15

GPIO.setup(12,GPIO.OUT)  # DISTANCE TRIGGER
GPIO.setup(16, GPIO.IN)  # DISTANCE ECHO

def forward():
	# Go forward
	print "Going forward"
	GPIO.output(7,True)
	GPIO.output(13,True)
	time.sleep(1)
	GPIO.output(7,False)
	GPIO.output(13,False)

def left():
	# Turn left
	print "Turning left"
	GPIO.output(7,True)
	GPIO.output(15,True)
	time.sleep(1)
	GPIO.output(7,False)
	GPIO.output(15,False)

def right():
	# Turn right
	print "Turning right"
	GPIO.output(13,True)
	GPIO.output(11,True)
	time.sleep(1)
	GPIO.output(13,False)
	GPIO.output(11,False)

def back():
	# Go backwards
	print "Going backwards"
	GPIO.output(11,True)
	GPIO.output(15,True)
	time.sleep(2)
	GPIO.output(11,False)
	GPIO.output(15,False)

def led():
	# Led blink
	print "Led blink 3 times"
	for b in range (0,3):
		GPIO.output(18,True)
		time.sleep(0.5)
		GPIO.output(18,False)
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
		
		if measure == 'cm':
				distance = tl / 0.000058
		elif measure == 'in':
				distance = tl / 0.000148
		else:
				print ('improper choise of measurement: in og cm')
				distance = None
				
		return distance
		
		

def main():
	# autonom main function
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(18, GPIO.OUT) # LED

		GPIO.setup(7, GPIO.OUT)  # MOTOR 1-7
		GPIO.setup(11,GPIO.OUT)  # MOTOR 2-11
		GPIO.setup(13,GPIO.OUT)  # MOTOR 3-13
		GPIO.setup(15,GPIO.OUT)  # MOTOR 4-15

		GPIO.setup(12,GPIO.OUT)  # DISTANCE TRIGGER
		GPIO.setup(16, GPIO.IN)  # DISTANCE ECHO
		
		distance = 0
		distance()
		
		if distance == distance < 15:
			blink()
			back()
			rints(0,2)
			if rints == 0:
				left()
			else:
				right()
		else:
			forward()
		GPIO.cleanup()


print(distance('cm'))

for x in range (0,20):
	main()
	time.sleep(0.1)
