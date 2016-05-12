import RPi.GPIO as GPIO
import time

def distance(measure='cm'):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(12,GPIO.OUT)
		GPIO.setup(16, GPIO.IN)
		
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
				
		GPIO.cleanup()
		return distance

print(distance('cm'))
