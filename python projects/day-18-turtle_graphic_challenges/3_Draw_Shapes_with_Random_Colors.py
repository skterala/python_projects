import random
from turtle import Turtle, Screen


my_tur = Turtle()

number_of_sides = 3
angle = 360

color = ['orchid', 'navy', 'tomato', 'goldenrod', 'slategray', 'aqua', 'crimson', 'khaki', 'teal', 'plum']

while number_of_sides <= 10:
    my_tur.color(random.choice(color))
    for _ in range(number_of_sides):
        my_tur.forward(100)
        my_tur.right(angle/number_of_sides)
    number_of_sides += 1

screen = Screen()
screen.exitonclick()