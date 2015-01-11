#!/usr/bin/env python3
import turtle
import random


def tree(branch_len, turtle_handle):
    random.seed()
    sub_len = random.randrange(5, 15)
    trunk_angle = random.randrange(15, 45)
    if branch_len > 5:
        turtle_handle.forward(branch_len)
        turtle_handle.right(trunk_angle)
        tree(branch_len - sub_len, turtle_handle)
        turtle_handle.left(trunk_angle)
        tree(branch_len - sub_len, turtle_handle)
        turtle_handle.right(trunk_angle)
        turtle_handle.backward(branch_len)

if __name__ == "__main__":
    turtle_handle = turtle.Turtle()
    myWin = turtle.Screen()
    turtle_handle.left(90)
    turtle_handle.up()
    turtle_handle.backward(100)
    turtle_handle.down()
    turtle_handle.color("green")
    tree(75, turtle_handle)
    myWin.exitonclick()
