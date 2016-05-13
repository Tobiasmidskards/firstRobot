import pygame, sys, termios
from pygame.locals import *
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(5, GPIO.OUT) 
GPIO.setup(6, GPIO.OUT) 
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(19, GPIO.OUT)


def turnleft(): 
	GPIO.output(13, GPIO.LOW) 
	GPIO.output(19, GPIO.HIGH) 
	GPIO.output(5, GPIO.LOW) 
	GPIO.output(6, GPIO.HIGH)

def forward():
	# Go forward
	print "Going forward"
	GPIO.output(11,True)
	GPIO.output(15,True)
	

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

def stahp():
	GPIO.output(13,False)
	GPIO.output(11,False)
	GPIO.output(15,False)
	GPIO.output(7,False)

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
		time.sleep(0.5)
		GPIO.output(18,False)
		time.sleep(0.5)
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

x=True

while x == True: 
	char = getch() 
	if(char == "w"): 
		forward() 
	if(char == "a"): 
		left() 
	if(char == "s"): 
		backward() 
	if(char == "d"): 
		right() 
	if(char == "k"): 
		stahp() 
	time.sleep(.02) 

print "cleanup"
GPIO.cleanup()







