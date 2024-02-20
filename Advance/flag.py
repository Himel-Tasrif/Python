# Tasrif Nur Himel

import turtle as t

def rectangle(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(300)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()

def circle(color):
    t.begin_fill()
    t.fillcolor(color)
    t.circle(-50)
    t.end_fill()

t.speed(0)  
t.up()
t.goto(0, -200)
t.down()
t.width(5)  
t.goto(0, 200)
t.width(1)  
rectangle('green')

t.goto(0, 170)
t.width(5)  
t.color('green')
t.forward(150)
t.width(1) 
circle('red')

t.done()  
