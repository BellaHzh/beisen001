# What will the following code draw?

import turtle

window = turtle.Screen()
window.setup(480, 480)
window.bgcolor('yellow')

draw1 = turtle.Turtle()
draw1.color('black', 'black')
draw1.pensize(1)
draw1.hideturtle()

draw2 = turtle.Turtle()
draw2.color('red')
draw2.pensize(4)
draw2.hideturtle()

draw1.penup()
draw1.forward(50)
draw1.pendown()
draw1.begin_fill()
draw1.circle(20)
draw1.end_fill()
draw1.penup()
draw1.backward(100)
draw1.pendown()
draw1.begin_fill()
draw1.circle(20)
draw1.end_fill()

draw2.penup()
draw2.left(220)
draw2.forward(100)
draw2.left(90)
draw2.pendown()
draw2.circle(100, 100)

window.mainloop()
