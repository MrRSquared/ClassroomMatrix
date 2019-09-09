#!/usr/bin/env python
# Display a runtext with double-buffering.

import os
import subprocess
from samplebase import SampleBase
from rgbmatrix import graphics, RGBMatrixOptions
import textwrap
import time
import csv


screen_width = 5 #width of screen in characters

class RunText(SampleBase):

    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
       
        
    
                

    def run(self):
        #Import the csv from the flash drive. In order to do this, one must enable the flash drive and create the mount point.
        with open('/mnt/flash/agenda.txt') as csv_file:
        #with open('agenda.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            data=list(csv.reader(csv_file, delimiter=','))
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("rpi-rgb-led-matrix/fonts/4x6.bdf")
        font2 = graphics.Font()
        font2.LoadFont("rpi-rgb-led-matrix/fonts/tom-thumb.bdf")
        textColor = graphics.Color(100, 100, 50)
        #First, we setup some constants.
        h = 6 # Font Height
        # pos1 = h+1
        pos = h+1
        hpos = 0
        new_pos = 6
        # line = 1
        count = 0
        def display_recycler(input):
            # The matrix cannot read multiline text independently, so we need to import the text
            # and format it so it fits the screen.
            # First we format our agenda...
            raw_text = input
            split_text = raw_text.splitlines(0)
            wrapped_display_text=[]
            #Then, we need to wrap long lines.
            for x in range(len(split_text)):
                wrapper = textwrap.fill(split_text [x], screen_width)
                w2 = "\n ".join(wrapper.split("\n"))
                wrapped_display_text.append(w2)

            display_text = '\n'.join(wrapped_display_text)
            wrapped_display_text = tuple(display_text.splitlines(0))
            print(wrapped_display_text)  
            return wrapped_display_text
        Categories = data[0]
        h1 = display_recycler(Categories[1])
        agenda = data[1][2]
        display_agenda = display_recycler(agenda)
        aLength = int((len(agenda)) / (4 -(len(h1)))) # to split the display text if it is too long. subtract the header in case it takes up multiple lines.
        # Objective

        while True:
            #offscreen_canvas.clear()
            for x in range(len(h1)):
                text = h1[x]
                projector = graphics.DrawText(offscreen_canvas, font2, 0 , hpos, textColor, text)
                hpos += new_pos
                pos = hpos
            
            # Agenda Loop
            for x in range(aLength):
                for x in range(len(display_agenda) - count):
                    my_text = display_agenda[x + count]
                    projector = graphics.DrawText(offscreen_canvas, font, 0 ,pos, textColor, my_text)
                    pos += new_pos
                    print(my_text) 

                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                    count += 1
                    time.sleep(10)
                    offscreen_canvas.Clear()
        
# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()   