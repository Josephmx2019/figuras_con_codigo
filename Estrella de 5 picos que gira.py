from turtle import *
from colorsys import *

t = Turtle()
s = Screen()
s.bgcolor("black")
t.speed(0)
n = 50
h = 0

for i in range(380):
    c = hsv_to_rgb(h,1,0.8)
    h = h + 1/n
    t.color(c)
    t.forward(i*2)
    t.left(145)
done()
