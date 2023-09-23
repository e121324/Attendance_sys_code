import turtle
from PIL import Image

wn = turtle.Screen()

wn.setup(640, 480)
wn.colormode(255)

turtle.speed(0)


def sqare(x,y, w,h):
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+w,y)
    turtle.goto(x+w,y-h)
    turtle.goto(x,y-h)
    turtle.goto(x,y)
    turtle.penup()
    turtle.end_fill()

turtle.color(252, 157, 3)
turtle.fillcolor(252, 157, 3)
sqare(-640,480, 50,50)

wn.exitonclick()
