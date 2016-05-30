import pygame
import RPi.GPIO as GPIO
import time
from random import randint as rints
#from sensor import distance

pygame.init()

done = False


while done == False:
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(40, GPIO.OUT) # LED RED
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # If user clicked close
        		done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        	if event.type == pygame.JOYBUTTONDOWN:
        		print("Joystick button pressed.")
        	if event.type == pygame.JOYBUTTONUP:
        		print("Joystick button released.")



	pygame.joystick.init()

	joystick_count = pygame.joystick.get_count()

	for i in range(joystick_count):
		joystick = pygame.joystick.Joystick(i)
		
		joystick.init()
		
		name = joystick.get_name()
		axes = joystick.get_numaxes()

		for i in range( axes ):
			axis = joystick.get_axis(i)

		buttons = joystick.get_numbuttons()

        for i in range( buttons ):
        	button = joystick.get_button( i )
       		hats = joystick.get_numhats()

       	if joystick.get_axis(1) < 0.0:
            		print (str(joystick.get_axis(1)))
            		print "jeg er ON"
            	
       	elif joystick.get_axis(1) > 0.0:
            		print (str(joystick.get_axis(1)))
            		print "jeg er OFF"
            		
       	#distance()
       	#print(distance('cm'))
       	GPIO.cleanup
            		
    GPIO.cleanup()
    

		
pygame.quit()
