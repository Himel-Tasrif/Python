import turtle
import colorsys

t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.speed(0)
n = 36
h = 0
for i in range(100):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h += 1/n
    t.color(c)
    t.left(145)
    for i in range(5):
        t.forward(300)
        t.left(150)
turtle.done()