import turtle as t
from turtle import Screen
import random


its = t.Turtle()


# its_turtle.shape("arrow")
# its_turtle.color("black")
# its_turtle.down()
# its_turtle.right(90)
# its_turtle.forward(100)
# its_turtle.right(90)
# its_turtle.forward(100)
# its_turtle.right(90)
# its_turtle.forward(100)
# its_turtle.right(90)
# its_turtle.forward

# for i in range(9):
#     its.forward(5)
#     its.penup()
#     its.forward(8)
# #     its.pendown()
# its.speed(300)
# for i in range(3):
#     its.forward(100)
#     its.right(120)
#
# for i in range(4):
#     its.forward(100)
#     its.right(90)
#
# for i in range(6):
#     its.forward(100)
#     its.right(60)
#
# for i in range(8):
#     its.forward(100)
#     its.right(45)
#
# for i in range(9):
#     its.forward(100)
#     its.right(40)
#     its.color("violet")
# for i in range(10):
#     its.forward(100)
#     its.right(36)
#     its.color("red")
# its.speed(3000)

# def shape(sides):
#     angle = 360/sides
#     for i in range(sides):
#         its.forward(100)
#         its.right(angle)
#
# for j in range(3,11):
#      shape(j)

# colors = ["purple", "blue", "green", "black","yellow", "sunflower"]
#
# direction=[0,90,180,270]
#
# its.pensize(15)
#
# for i in range(30):
#     its.color(random.choice(colors))
#     its.forward(30)
#     its.setheading(random.choice(direction))

t.colormode(255)
def colorm():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    c = (r, g, b)
    return c
colorm()
its.speed(500)
for i in range(40):
    current = its.heading()
    its.width(1)
    its.color(colorm())
    its.left(10)
    its.circle(130)
    its.setheading(current+10)

screen = Screen()
screen.exitonclick()