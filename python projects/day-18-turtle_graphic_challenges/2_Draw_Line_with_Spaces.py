# Draw a straight line with spaces in between.

import turtle as tur

my_turtle = tur.Turtle()

for _ in range(20):
    my_turtle.pendown()
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)

screen = tur.Screen()
screen.exitonclick()