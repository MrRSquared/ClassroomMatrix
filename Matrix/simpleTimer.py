#!/usr/bin/env python
# Display a timer.
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = 0
        my_text = self.args.text
        min = 2
        sec = 0
        min_converted = min*60
        t = min_converted + sec

        while True:
            offscreen_canvas.Clear()
            mins, secs = divmod(t,60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            t -= 1
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, time_format)
            time.sleep(1)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
