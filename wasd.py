import pygame, sys, termios, tty
from pygame.locals import *
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(7, GPIO.OUT) 
GPIO.setup(11, GPIO.OUT) 
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)


def left():
	# Go forward
	print "Going forward"
	GPIO.output(11,True)
	GPIO.output(15,True)
	

def back():
	# Turn left
	print "Turning left"
	GPIO.output(7,True)
	GPIO.output(15,True)
	

def forward():
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

def right():
	# Go backwards
	print "Going backwards"
	GPIO.output(7,True)
	GPIO.output(13,True)

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


while True: 
		GPIO.setmode(GPIO.BOARD) 
		GPIO.setup(7, GPIO.OUT) 
		GPIO.setup(11, GPIO.OUT) 
		GPIO.setup(13, GPIO.OUT) 
		GPIO.setup(15, GPIO.OUT)
		GPIO.setup(18, GPIO.OUT)

	
		char = getch() 
		if(char == "w"): 
			forward() 
		if(char == "a"): 
			left() 
		if(char == "s"): 
			back() 
		if(char == "d"): 
			right() 
		else:
			stahp() 
		time.sleep(.02) 


print "cleanup"
GPIO.cleanup()







