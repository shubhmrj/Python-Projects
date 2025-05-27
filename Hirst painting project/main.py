import turtle
from turtle import Screen
import turtle as t
import random
its = t.Turtle()

# import colorgram

#
# example = []
# colors = colorgram.extract("hirst.jpg", 6)
# firstcolor = colors[0]
#
# rgb = firstcolor.rgb
# hsl = firstcolor.hsl
# proportion=firstcolor.proportion
#
# red = rgb[1]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple2 = (r, g, b)
#     example.append(tuple2)
#
# print(example)
its.hideturtle()
its.penup()
color_gram = [(248, 247, 244), (243, 250, 247), (250, 244, 248), (241, 244, 248), (5, 12, 35), (40, 21, 16)]
t.colormode(255)
its.speed("fastest")
its.setheading(225)
its.forward(250)
its.setheading(0)
# nod = 100
for i in range(1,101):
    its.dot(20, random.choice(color_gram))
    its.forward(50)

    if i % 10 == 0:
        its.setheading(90)
        its.forward(50)
        its.setheading(180)
        its.forward(500)
        its.setheading(0)

screen = Screen()
screen.exitonclick()