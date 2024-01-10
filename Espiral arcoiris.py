from turtle import *

speed(15)
bgcolor("black")
r, g, b = 255, 0 , 0

for i in range(255*2):
    colormode(255)

    if i<(255*1)//3:
        g +=3
    elif i<(255*2)//3:
        r-=3
    elif i<(255*3)//3:
        b+=3
    elif i<(255*4)//3:
        g-=3
    elif i<(255*5)//3:
        r+=3

    forward(50+i)
    right(91)
    pencolor(r,g,b)

done()
