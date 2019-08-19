#!/usr/bin/env python

"""This is the code for direct interaction for our timer.

Our main encoder code is borrowed from This code is courtesy of hrvoje.
It can be found here. https://www.raspberrypi.org/forums/ """

from gpiozero import Button
import time

pin_a = Button(2, pull_up = True)
pin_b = Button(3, pull_up = True)

button = Button(4, pull_up = True)
reset = Button(5, pull_up = True)



def ticker():
    
    while True:
    
        # If dial is turned up, increase minutes
        if pin_a.is_pressed:
             minutes += 1
             
        # If dial is turned down, decrease minutes
        if pin_b.is_pressed:
            minutes -= 1

        setminutes = minutes
        # Jump to seconds
        if button.is_pressed: break

        else:
            setminutes = minutes

        formatted = '{:02d}:{:02d}'.format(minutes, seconds)
                
        print (formatted, end = '\r')

    while True:
        # If dial is turned up, increase seconds
        if pin_a.is_pressed:
             seconds += 1
             
        # If dial is turned down, decrease seconds
        if pin_b.is_pressed:
            seconds -= 1
        # Jump to seconds
        if button.is_pressed: break

        formatted = '{:02d}:{:02d}'.format(minutes, seconds)
                
        print (formatted, end = '\r')

        setseconds = seconds
        
    return (setminutes, seconds)

        
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
minutes = 0
seconds = 0

ticker()

timer = ticker()
print (timer)
countdown(*timer)

quit()

__author__ = "Jacob Roth-Ritchie"
__copyright__ = "Copyright 20019, RSquar3dT3ch"
__license__ = "GPL"
__version__ = ".01"
__maintainer__ = "Jacob Roth-Ritchie"
__email__ = "jrothritchie@hdsd.org"
__status__ = "Development"
