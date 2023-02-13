import turtle
from turtle import Turtle, colormode
from colour import colours
import random
from random import randint
colormode(255)

timmmy_the_turtle = Turtle()
timmmy_the_turtle.shape("turtle")
timmmy_the_turtle.color("red")



def draw_shape():
    timmmy_the_turtle.forward(70)
    timmmy_the_turtle.left(rotate_angle)


for _ in range(3, 15):
    timmmy_the_turtle.color(random.choice(colours))
    sides = _
    sum_of_angles = (sides - 2) * 180
    each_angle = sum_of_angles / sides
    rotate_angle = 180 - each_angle
    for times in range(sides):
        draw_shape()


screen = turtle.Screen()
screen.exitonclick()