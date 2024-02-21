# Tasrif Nur Himel

import turtle

# Screen Setup
new = turtle.getscreen()
new.bgcolor("black")

# Create the Sun
sun = turtle.Turtle()
sun.speed(0)
sun.color("red")
sun.shape("circle")
sun.penup()
sun.goto(0, 0)  
sun.pendown()
sun.shapesize(stretch_wid=8, stretch_len=8)  

# Pen for Writing Numbers
dpen = turtle.Turtle()
dpen.width(3)
dpen.color("white")
dpen.speed(10)

# Hidden Work (penup)
dpen.left(180)
dpen.penup()
dpen.forward(270)
dpen.left(90)
dpen.forward(200)
dpen.left(180)
dpen.pendown()


def draw_1():
    # Start to draw
    dpen.forward(200) #
    dpen.right(90)
    dpen.forward(55)
    dpen.right(90)
    dpen.forward(200) #
    dpen.right(90)
    dpen.forward(10)
    dpen.right(90)
    dpen.forward(190) #
    dpen.left(90)
    dpen.forward(35)
    dpen.left(90)

    

    dpen.forward(190) #
    dpen.right(90)
    dpen.forward(10)

    dpen.penup()
    dpen.left(180)
    dpen.forward(75)
    dpen.left(90)
    dpen.pendown()


def draw_2():
    dpen.forward(270)
    dpen.right(90)
    dpen.forward(55)
    dpen.right(90)
    dpen.forward(270)
    dpen.right(90)
    dpen.forward(10)
    dpen.right(90)
    dpen.forward(260)
    dpen.left(90)
    dpen.forward(35)
    dpen.left(90)
    dpen.forward(260)
    dpen.right(90)
    dpen.forward(10)

    dpen.penup()
    dpen.left(180)
    dpen.forward(110)
    dpen.left(90)
    dpen.pendown()

def draw_3():
    
    dpen.forward(290)
    dpen.left(15)
    dpen.forward(150)
    dpen.right(105)
    dpen.forward(252.6457135)
    dpen.right(105)
    dpen.forward(150)
    dpen.left(15)
    dpen.forward(290)
    dpen.right(90)
    dpen.forward(15)
    dpen.right(90)
    dpen.forward(290)
    dpen.right(15)
    dpen.forward(140)
    dpen.left(105)
    dpen.forward(125.5454112)
    dpen.left(100)
    dpen.forward(140)
    dpen.right(10)
    dpen.forward(290)
    dpen.right(90)
    dpen.forward(15)
    dpen.right(90)
    dpen.forward(290)
    dpen.left(10)
    dpen.forward(140)
    dpen.left(80)
    dpen.forward(76.74131845)
    dpen.left(105)
    dpen.forward(140)
    dpen.right(15)
    dpen.forward(290)
    dpen.right(90)
    dpen.forward(15)

    dpen.penup()
    dpen.left(180)
    dpen.forward(225)
    dpen.left(90)

    dpen.pendown()

def draw_4():
    dpen.forward(270)
    dpen.right(90)
    dpen.forward(55)
    dpen.right(90)
    dpen.forward(270)
    dpen.right(90)
    dpen.forward(10)
    dpen.right(90)
    dpen.forward(260)
    dpen.left(90)
    dpen.forward(35)
    dpen.left(90)
    dpen.forward(260)
    dpen.right(90)
    dpen.forward(10)

    dpen.penup()
    dpen.left(180)
    dpen.forward(75)
    dpen.left(90)

    dpen.pendown()

draw_1()
draw_2()
draw_3()
draw_4()
draw_1() 

dpen.penup()
dpen.left(90)
dpen.forward(40)
dpen.right(90)
dpen.forward(360)
dpen.left(180)
dpen.forward(142.5)


x_axis = turtle.Turtle()
x_axis.speed(0)
x_axis.color("white")
x_axis.penup()
x_axis.goto(-300, -202.5)
x_axis.pendown()
x_axis.forward(600)
x_axis.hideturtle()
turtle.done()