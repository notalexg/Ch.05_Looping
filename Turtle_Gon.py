''' # Actual assignment
import turtle
sdnum = int(input("How many sides?"))
tgon = turtle.Turtle()
tgon.shape('turtle')
for i in range (sdnum):
    tgon.fd(100)
    tgon.left(360/sdnum)
turtle.Screen().exitonclick()
'''

import turtle # For fun assignment
sdnum = int(input("How many sides?"))
color = input("What color would you like it to be?")
tgon = turtle.Turtle()
tgon.turtlesize(1)
tgon.shape('arrow')
tgon.color(color)
tgon.begin_fill()
tgon.fillcolor(color)
tgon.speed(1000)

for i in range (sdnum):
    tgon.fd(100/(sdnum/5))
    tgon.left(360/sdnum)
tgon.end_fill()
tgon.hideturtle()

turtle.Screen().exitonclick()