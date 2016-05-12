import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

def distance(measure='cm'):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(12,GPIO.OUT)
		GPIO.setup(16, GPIO.IN)
		GPIO.setup(18, GPIO.OUT)
		
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
		
		if distance == distance < 10:
			GPIO.output(18,True)
			time.sleep(0.1)
			GPIO.output(18,False)
		else:
			GPIO.output(18,False)
				
		GPIO.cleanup()
		
		return distance

print(distance('cm'))

for x in range (0,20):
	time.sleep(0.1)
	print(distance('cm'))
