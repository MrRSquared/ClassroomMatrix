import time
from gpiozero import Button

pin_a = Button(2, pull_up = True)
pin_b = Button(3, pull_up = True)

button = Button(4, pull_up = True)


def ticker(counter):
    while True:
    
        # If dial is turned up, increase minutes
        if pin_a.is_pressed:
             counter += 1
             
        # If dial is turned down, decrease minutes
        if pin_b.is_pressed:
            counter -= 1
        # Jump to seconds
        if button.is_pressed:
            print ('The counter is bieng reset becaused you pressed the button')
            counter = 0
                
        print (counter, end = '\r')
             
ticker(0)
quit()
