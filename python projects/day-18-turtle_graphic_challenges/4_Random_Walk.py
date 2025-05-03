import random
from turtle import Turtle, Screen

my_turtle = Turtle()

color = ['orchid', 'navy', 'tomato', 'goldenrod', 'slategray', 'aqua', 'crimson', 'khaki', 'teal', 'plum']
directions = [0, 90, 180, 270]
my_turtle.width(10)
my_turtle.speed("fastest")

for _ in range(100):
    my_turtle.color(random.choice(color))
    my_turtle.forward(50)
    my_turtle.right(random.choice(directions))

screen = Screen()
screen.exitonclick()