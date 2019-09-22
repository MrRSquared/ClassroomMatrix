#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
#!/usr/bin/env python
import os
import subprocess
import csv
from rgbmatrix import graphics, RGBMatrixOptions
import textwrap
import time


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)


    def run(self):
        # Create constants
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("rpi-rgb-led-matrix/fonts/4x6.bdf")
        font2 = graphics.Font()
        font2.LoadFont("rpi-rgb-led-matrix/fonts/tom-thumb.bdf")
        textColor = graphics.Color(100, 100, 50)
        textColor2 = graphics.Color(100, 20, 100)
        pos = offscreen_canvas.width
        
	# Get the file
        with open('/mnt/flash/agenda.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            data=list(csv.reader(csv_file, delimiter=','))
	
        print (data)
        agenda = data[1][2]
        Objective = data[1][1]
        Categories = data[0]
        homework = data[1][3]
        
        h= 6 # Font Height
        pos1 = h+1
        pos = h+1
        new_pos = h
        line = 1
        print('agenda is' +agenda)
        print(type(agenda))
        Objective = tuple(Objective.splitlines(0))
        agenda = agenda.splitlines(0)
        print(type(agenda))
        new_agenda = []
        for x in range(len(agenda)):
            wrapper = textwrap.fill(agenda [x], 18)
            w2 = "\n".join(wrapper.split("\n"))
            new_agenda.append(w2)
        a = '\n'.join(new_agenda)
        print(a)
        a = a.splitlines(0)
        homework = homework.splitlines(0)
        aLength = int((len(agenda)) / 3)
        print (a)
        count = 0
            

        
        while True:
            # Objective
            h1 = Categories[1]
            stuff = graphics.DrawText(offscreen_canvas, font2, 0 , pos, textColor2, h1)
            pos += new_pos
            
            for x in range (len(Objective)):
                h1 = Objective[x]
                stuff = graphics.DrawText(offscreen_canvas, font2, 0 , pos, textColor, h1)
                pos += new_pos
            
            
            # Agenda Loop
            h1 = Categories[2]
            stuff = graphics.DrawText(offscreen_canvas, font2, 0 , pos, textColor2, h1)
            pos += new_pos

            for x in range(aLength):
                for x in range(len(a) - count):
                    # 1st display
                    #offscreen_canvas.Clear()
                    my_text = a[x + count]
                    # print(my_text)
                    stuff = graphics.DrawText(offscreen_canvas, font, 0 ,pos, textColor, my_text)
                    pos += new_pos
                    print(my_text) 
                    #prev = x  
                    #second display
                    #if x > 3:
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                time.sleep(10)
                offscreen_canvas.Clear()

                #Homework:
                h1 = Categories[3]
                stuff = graphics.DrawText(offscreen_canvas, font2, 0 , pos, textColor2, h1)
                pos += new_pos

                for x in range(len(homework)):
                    my_text = homework[x]
                    # print(my_text)
                    stuff = graphics.DrawText(offscreen_canvas, font, 0 ,pos, textColor, my_text)
                    pos += new_pos
                    print(my_text)
      
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                count += 3
                time.sleep(10)
            
 

            
            offscreen_canvas.Clear()
            count = 0
            pos = pos1         
            # pos =0
            stuff2 = graphics.DrawText(offscreen_canvas, font, 0 ,pos, textColor, "")
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            time.sleep(2)
            

            

# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
