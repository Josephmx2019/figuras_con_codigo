from turtle import *

title("      Feliz navidad:)")
a = Turtle()
a.getscreen().bgcolor("black")
a.penup()
a.goto(-215,50)
a.pendown()
a.color("#AACDE2")
a.speed(25)

def star(turtle,size):
    if size<=10:
        return
    else:
        begin_fill()
        for i in range(5):
            pensize(2)
            forward(size)
            star(turtle,size/3)
            left(216)
            end_fill()

star(a,380)
done()
