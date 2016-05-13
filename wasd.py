import pygame, sys, termios, tty
from pygame.locals import *
import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(7, GPIO.OUT) 
GPIO.setup(11, GPIO.OUT) 
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

def forward():
	# Go forward
	print "Going forward"
	GPIO.output(11,True)
	GPIO.output(15,True)
	

def right():
	# Turn left
	print "Turning left"
	GPIO.output(7,True)
	GPIO.output(15,True)
	

def left():
	# Turn right
	print "Turning right"
	GPIO.output(13,True)
	GPIO.output(11,True)


def stahp():
	# Stop
	print "Stopping all motors"
	GPIO.output(13,False)
	GPIO.output(11,False)
	GPIO.output(15,False)
	GPIO.output(7,False)

def back():
	# Go backwards
	print "Going backwards"
	GPIO.output(7,True)
	GPIO.output(13,True)


def led():
	# Led blink
	print "Led blink 3 times"
	for b in range (0,3):
		GPIO.output(18,True)
		time.sleep(0.25)
		GPIO.output(18,False)
		time.sleep(0.25)
def getch(): 
	fd = sys.stdin.fileno() 
	old_settings = termios.tcgetattr(fd) 
	try: 
		tty.setraw(sys.stdin.fileno()) 
		ch = sys.stdin.read(1) 
	finally: 
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) 
	return ch

time.sleep(.5) 
print("Use WASD to drive") 
time.sleep(.5) 
print("'K' Will stop the drive motors") 

def on():
	
   while True: 
	GPIO.setmode(GPIO.BOARD) 
	GPIO.setup(7, GPIO.OUT) 
	GPIO.setup(11, GPIO.OUT) 
	GPIO.setup(13, GPIO.OUT) 
	GPIO.setup(15, GPIO.OUT)
	
	char = getch() 
	if(char == "w"): 
		forward() 
	if(char == "a"): 
		left() 
	if(char == "s"): 
		back() 
	if(char == "d"): 
		right() 
	if(char == "k"): 
		stahp() 
	if(char == "b"): 
		led()
	time.sleep(.02) 

f = on()
f.daemon = True
f.start()

print "cleanup"
GPIO.cleanup()







