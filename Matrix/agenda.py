#!/usr/bin/env python
# Display a runtext with double-buffering.

import os
import subprocess
from samplebase import SampleBase
from rgbmatrix import graphics, RGBMatrixOptions
import textwrap
import time
import csv


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)


    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("rpi-rgb-led-matrix/fonts/4x6.bdf")
        font2 = graphics.Font()
        font2.LoadFont("rpi-rgb-led-matrix/fonts/tom-thumb.bdf")
        textColor = graphics.Color(100, 100, 50)
        pos = offscreen_canvas.width
        
        with open('/mnt/flash/agenda.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            data=list(csv.reader(csv_file, delimiter=','))

        agenda = data[1][2]
        Objective = data[1][1]
        Categories = data[1]
        h= 6 # Font Height
        pos1 = h+1
        pos = h+1
        new_pos = 6
        line = 1
        print('agenda is' +agenda)
        print(type(agenda))
        agenda = agenda.splitlines(0)
        print(type(agenda))
        new_agenda = []
        for x in range(len(agenda)):
            wrapper = textwrap.fill(agenda [x], 6)
            w2 = "\n".join(wrapper.split("\n"))
            new_agenda.append(w2)
        a = '\n'.join(new_agenda)
        print(a)
        a = a.splitlines(0)
        Objective = tuple(Objective.splitlines(0))
        aLength = int((len(agenda)) / 3)
        print (a)
        count = 0
            

        
        while True:
            #offscreen_canvas.clear()
            h1 = Categories[1]
            stuff = graphics.DrawText(offscreen_canvas, font2, 0 , pos, textColor, h1)
            pos += new_pos
            
            # Agenda Loop
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
                count += 3
                time.sleep(10)
                offscreen_canvas.Clear()
            
            count = 0
            pos = pos1
            h2 = Categories[1]
            stuff2 = graphics.DrawText(offscreen_canvas, font, 0 ,pos, textColor, h2)
            pos += new_pos
            time.sleep(1)
         
            
            for x in range(len(Objective)):
                time.sleep(1)
                my_text = Objective[x]
                stuff = graphics.DrawText(offscreen_canvas, font, 0 ,pos, textColor, my_text)
                pos += new_pos
                print(my_text)     
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            time.sleep(10)

            

# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
