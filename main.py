import turtle
from turtle import Turtle, Screen
from random import choice
scr = Screen()
t = Turtle()

def go():
    t.forward(10)
def up():
    t.setheading(90)
    t.forward(20)


def nowrite():
    t.penup()
    t.forward(10)
    t.pendown()

def right():
    t.setheading(0)
    t.forward(10)

def left():
    t.setheading(180)
    t.forward(10)

def reverse():
    t.setheading(270)
    t.forward(10)

def lright():
    t.right(10)

def lleft():
    t.left(10)

def color():
    t.color(choice(["red", "blue", "green", "black", "pink", "orange", "grey"]))


scr.listen()

scr.onkey(key = "space", fun = nowrite)
scr.onkey(key = "w", fun = up)
scr.onkey(key = "a", fun = left)
scr.onkey(key = "d", fun = right)
scr.onkey(key = "s", fun = reverse)
scr.onkey(key = "p", fun = lright)
scr.onkey(key = "o", fun = lleft)
scr.onkey(key = "c", fun = color)
scr.onkey(key = "b", fun = go)



scr.exitonclick()
