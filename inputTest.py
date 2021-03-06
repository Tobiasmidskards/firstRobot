import RPi.GPIO as GPIO
import time
from random import randint as rints
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT) # LED WHITE
GPIO.setup(40, GPIO.OUT) # LED RED

GPIO.setup(7, GPIO.OUT)  # MOTOR 1-7
GPIO.setup(11,GPIO.OUT)  # MOTOR 2-11
GPIO.setup(13,GPIO.OUT)  # MOTOR 3-13
GPIO.setup(15,GPIO.OUT)  # MOTOR 4-15

GPIO.setup(12,GPIO.OUT)  # DISTANCE TRIGGER
GPIO.setup(16, GPIO.IN)  # DISTANCE ECHO

print ("1 - Fremad")
print ("2 - Bagud")
print ("3 - Hojre")
print ("4 - Venstre")
print ("5 - Lys")

tid = 5

def count():
	print "1 ud af 5 sekunder"
	time.sleep(1)
	print "2 ud af 5 sekunder"
	time.sleep(1)
	print "3 ud af 5 sekunder"
	time.sleep(1)
	print "4 ud af 5 sekunder"
	time.sleep(1)
	print "5 ud af 5 sekunder"
	time.sleep(1)
	
def stop():
	print ("Stopper test")
	GPIO.output(7,False)
	GPIO.output(11,False)
	GPIO.output(13,False)
	GPIO.output(15,False)
	GPIO.output(18,False)
	GPIO.output(40,False)

def forward():
	print ("Korer fremad")
	GPIO.output(7,True)
	GPIO.output(13,True)
	count()
	stop()

def backward():
	print ("Korer baglaens")
	GPIO.output(11,True)
	GPIO.output(15,True)
	count()
	stop()

def left():
	print ("Drejer til venstre")
	GPIO.output(7,True)
	GPIO.output(15,True)
	count()
	stop()

def right():
	print ("Drejer til hojre")
	GPIO.output(11,True)
	GPIO.output(13,True)
	count()
	stop()

def light():
	print ("Taender lys")
	GPIO.output(18,True)
	GPIO.output(40,True)
	count()
	stop()

def main():
	stop()
	hvad = input ('Hvad vil du teste?: ')
	if hvad == 1:
		forward()
	elif hvad == 2:
		backward()
	elif hvad == 3:
		right()
	elif hvad == 4:
		left()
	elif hvad == 5:
		light()
	else:
        	print ("Skriv det ordenligt.")

main()

