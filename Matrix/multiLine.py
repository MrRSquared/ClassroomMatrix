#!/usr/bin/env python

"""This code displays our agenda and objectives for the day.  It reads a text file placed on a flash drive on the pi.  It is adapted from
Henner Zeller's runtext example found in ~/bindings/python/samples. """

from samplebase import SampleBase
from rgbmatrix import graphics, RGBMatrixOptions
import textwrap
import time


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)


    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/tom-thumb.bdf")
        font2 = graphics.Font()
        font2.LoadFont("../../../fonts/6x9.bdf")
        textColor = graphics.Color(100, 100, 50)
        pos = offscreen_canvas.width
        a = ["Line1", "Line2", "Line3"]
        b = ["Header", "Line4", "Line5", "Line6"]
        c = ["Today we will...", "So that we can..."]
        h= 4 # Font Height
        pos1 = h+1
        pos = h+1
        new_pos = 6
        line = 1

        while True:
            #offscreen_canvas.clear()
            h1 = c[0]
            stuff = graphics.DrawText(offscreen_canvas, font2, 0 ,pos, textColor, h1)
            pos += new_pos
            for x in range(len(a)):
                # 1st display
                #offscreen_canvas.Clear()
                my_text = a[x]
                stuff = graphics.DrawText(offscreen_canvas, font, 20 ,pos, textColor, my_text)
                pos += new_pos
                print(my_text) 
                #prev = x  
                #second display
                #if x > 3:

                      
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            time.sleep(10)
            offscreen_canvas.Clear()
            pos = pos1
            h2 = c[1]
            stuff2 = graphics.DrawText(offscreen_canvas, font, 0 ,pos, textColor, h2)
            pos += new_pos
            time.sleep(1)
            for x in range(len(b)):
                time.sleep(1)
                my_text = b[x]
                stuff = graphics.DrawText(offscreen_canvas, font, 20 ,pos, textColor, my_text)
                pos += new_pos
                print(my_text)     
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            time.sleep(20)

            

# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()


__author__ = "Jacob Roth-Ritchie"
__copyright__ = "Copyright 20019, RSquar3dT3ch"
__license__ = "GPL 3.0"
__version__ = ".01"
__maintainer__ = "Jacob Roth-Ritchie"
__email__ = "jrothritchie@hdsd.org"
__status__ = "Development"
