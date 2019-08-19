#!/usr/bin/env python

"""This is the code for direct interaction for our timer.

Our main encoder code is borrowed from This code is courtesy of hrvoje.
It can be found here. https://www.raspberrypi.org/forums/ """

import time
import RPi.GPIO as GPIO
import threading
Enc_A = 2  				# Encoder input A: input GPIO 4 
Enc_B = 3  			        # Encoder input B: input GPIO 14 
Button = 4              #Encoder button

Rotary_counter = 0  			# Start counting from 0
Current_A = 1					# Assume that rotary switch is not 
Current_B = 1					# moving while we init software

LockRotary = threading.Lock()		# create lock for rotary switch
	

# initialize interrupt handlers
def init():
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(Button,GPIO.IN, pull_up_down = GPIO.PUD_UP)

    GPIO.setup(Enc_A, GPIO.IN) 				
    GPIO.setup(Enc_B, GPIO.IN)
    
    GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotary_interrupt) 				# NO bouncetime 
    GPIO.add_event_detect(Enc_B, GPIO.RISING, callback=rotary_interrupt) 				# NO bouncetime 

    return

def Mover_button():
    global Move_on
    Move_on = GPIO.input(Button)
    #return

# Rotarty encoder interrupt:
# this one is called for both inputs from rotary switch (A and B)
def rotary_interrupt(A_or_B):
	global Rotary_counter, Current_A, Current_B, LockRotary, Move_on
													# read both of the switches
	Switch_A = GPIO.input(Enc_A)
	Switch_B = GPIO.input(Enc_B)
													# now check if state of A or B has changed
													# if not that means that bouncing caused it
	if Current_A == Switch_A and Current_B == Switch_B:		# Same interrupt as before (Bouncing)?
		return										# ignore interrupt!

	Current_A = Switch_A								# remember new state
	Current_B = Switch_B								# for next bouncing check


	if (Switch_A and Switch_B):						# Both one active? Yes -> end of sequence
		LockRotary.acquire()						# get lock 
		if A_or_B == Enc_B:							# Turning direction depends on 
			Rotary_counter += 1						# which input gave last interrupt
		else:										# so depending on direction either
			Rotary_counter -= 1						# increase or decrease counter
		LockRotary.release()						# and release lock
	return	

#Calculate minutes reading, direction and speed of turning left/rignt
def minutes(minutes):
    global minn, Rotary_counter, LockRotary, Move_on

    NewCounter = 0
    

    init() 
    Mover_button()

    while True:
        time.sleep(0.1)								# sleep 100 msec

        LockRotary.acquire()					# get lock for rotary switch
        NewCounter = Rotary_counter			# get counter value
        Rotary_counter = 0						# RESET IT TO 0
        LockRotary.release()					# and release lock
					
        if (NewCounter !=0):					# Counter has CHANGED
            minutes = minutes + NewCounter*abs(NewCounter)	# Decrease or increase minutes
        minn = minutes
        # Jump to seconds
        
        if Move_on == False:
            break

        formatted = '{:02d}:{:02d}'.format(minutes, 0)
                
        print (formatted, end = '\r')
        
    
def countdown(min, sec):

    min_converted = int(min)*60
    t = min_converted + int(sec)
    while t:
        
        mins, secs = divmod(t,60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print (timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Time is up!!!! \n\n\n\n\n')

secc = 0
minutes(0)
# seconds(0)
countdown(minn, secc)

quit()


__author__ = "Jacob Roth-Ritchie"
__copyright__ = "Copyright 20019, RSquar3dT3ch"
__license__ = "GPL"
__version__ = ".01"
__maintainer__ = "Jacob Roth-Ritchie"
__email__ = "jrothritchie@hdsd.org"
__status__ = "Development"
