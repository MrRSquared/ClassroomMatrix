import time
from gpiozero import Button

pin_a = Button(2, pull_up = True)
pin_b = Button(3, pull_up = True)

button = Button(4, pull_up = True)

def ticker(minutes, seconds):
    while True:
    
        # Check if rotary encoder went up
        if pin_a.is_pressed:
             minutes += 1
             #print (counter)
        
        if pin_b.is_pressed:
            minutes -= 1
            #print (counter)

        if button.is_pressed:
            #print("resetting counter because you pressed the button.")
            minutes = 0
        #else:
            #minutes += 1
        #    if minutes >= 300: break
        print (minutes, seconds, end = '\r')
    #while True:
    #    seconds -= 1
    #    print (minutes, seconds, end = '\r')
             
ticker(200, 100)
quit()
