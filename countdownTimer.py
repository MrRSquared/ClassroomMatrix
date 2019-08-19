import time


def countdown(min, sec):

    min_converted = min*60
    t = min_converted + sec
    while t:
        
        mins, secs = divmod(t,60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print (timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Time is up!!!! \n\n\n\n\n')


minutes = input('Enter the desired minutes : ')
seconds = input('Enter the desired seconds : ')
countdown(int(minutes), int(seconds))
quit()
