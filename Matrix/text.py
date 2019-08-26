#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")

        blue = graphics.Color(0, 0, 255)
        graphics.DrawText(canvas,font,0,6,graphics.Color(255,0,0),"Test 123")
        graphics.DrawText(canvas,font,0,12,graphics.Color(0,255,0),"Text 123")
        graphics.DrawText(canvas,font,0,18,graphics.Color(0,0,255),"For 1234")


        time.sleep(10)   # show display for 10 seconds before exit
        blue = graphics.Color(0, 0, 255)
        graphics.DrawText(canvas, font, 2, 9, blue, 
        "newText"
        "as ks this")
        time.sleep(10)

# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
