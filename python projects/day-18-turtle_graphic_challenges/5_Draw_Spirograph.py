import random
from turtle import Turtle, Screen

my_turtle = Turtle()
angle = 10
number_of_circles = int(360/angle)
my_turtle.speed("fastest")

color = ['orchid', 'navy', 'tomato', 'goldenrod', 'slategray', 'aqua', 'crimson', 'khaki', 'teal', 'plum']

for _ in range(number_of_circles):
    my_turtle.color(random.choice(color))
    my_turtle.circle(radius=100)
    my_turtle.right(angle)


screen = Screen()
screen.exitonclick()