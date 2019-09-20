#!/usr/bin/env python
"""
A script to generate SVG icon for the personal blog.
"""
import svgwrite

width = 256
height = 256
mtop = mbottom = mright = mleft = 256/8

dwg = svgwrite.Drawing(filename="blog_icon.svg", size=(height, width))

def draw_pattern(width, color):
    xpos = 256/8 + mleft
    ypos = 256/8
    increment = 256*2/8
    vlines = dwg.add(dwg.g(id="vlines", stroke=color, stroke_width=width, stroke_linecap="round"))
    hlines = dwg.add(dwg.g(id="vlines", stroke=color, stroke_width=width, stroke_linecap="round"))
    while (xpos < 256*7/8):
        vlines.add(dwg.line(start=(xpos,ypos), end=(xpos, 256 - mbottom)))
        hlines.add(dwg.line(start=(mleft, ypos), end=(xpos+mright, ypos)))
        xpos += increment
        ypos += increment

draw_pattern(20, "black")
draw_pattern(8, "white")

dwg.save(pretty=True)
