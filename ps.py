import pygame

pygame.init()

done = False


while done == False:

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

		name = joystick.get_name()
		axes = joystick.get_numaxes()

		for i in range( axes ):
			axis = joystick.get_axis(i)

		buttons = joystick.get_numbuttons()

        	for i in range( buttons ):
            		button = joystick.get_button( i )

        		hats = joystick.get_numhats()


		#tester
        	if joystick.get_hat(0) == (0,1):
            		x()

pygame.quit()
