#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
from mandelbrot import *

filename = "mandelbrot.png"

print ("#------------------------------------------------------#")
print ("#                    MANDELBROT SET                    #")
print ("#------------------------------------------------------#")
x1 = int(input("Introduce the value for x1 --> "))
y1 = int(input("Introduce the value for y1 --> "))
x2 = int(input("Introduce the value for x2 --> "))
y2 = int(input("Introduce the value for y2 --> "))
width = int(input("Introduce the value for the width --> "))
iters = int(input("Introduce the value for the iterations --> "))

print ("\nDepending on the size, this can be take time...")
renderizaMandelbrot(x1, y1, x2, y2, width, iters, filename)
print ("\nDone!")
