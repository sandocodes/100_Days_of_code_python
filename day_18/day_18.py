# Understanding Python Turtle Module
import turtle as t

screen = t.Screen()
tim = t.Turtle()

#Example 1. Draw a Sqare 100 x 100
def turtle_square():
    for _ in range(4): 
        tim.forward(100)
        tim.right(90)
# turtle_square()


#Example 2. Draw Dashed Line
def dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()
# dashed_line()

#Example 3. Drawing Different Shapes with different colors from triangle(3) to pentagon(10)
    # Square = 90deg angle
    # Pentagon = 72deg angle
    # 360 / sides = Working out shape's angle


# Random Colors
import random

t.colormode(255)
# color_list = ["red", "blue", "green", "purple", "medium violet red", "chartreuse", "sienna", "indian red", "olive drab", "slate gray"]
# my_color = random.choice(color_list)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color


def random_shape():
    for shape_sides in range(3, 11):
        tim.color(random_color())
        for _ in range(shape_sides):
            shape_angle = 360 / shape_sides
            tim.forward(100)
            tim.right(shape_angle)
# random_shape()


# STAR
            
def star_shape():
    for _ in range(5):
        angle = 145
        tim.forward(100)
        tim.right(angle)
        tim.forward(100)
# star_shape()

############################################
#       Example 4. Draw a Random Walk
############################################

directions = [0, 90, 180, 270]

tim.pensize(15)
tim.speed("fastest")

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


#Example 5. Draw a Spirograph - Number of circle, each with a radius of 100 in distance. Use random colors and the Turtle documentation
# Draw different number of circle
# Each circle with a radius of 100 in distance


def draw_spirograph(size_of_gap):
    # make pencil thin
    tim.pensize(1)

    for _ in range(int(360 / size_of_gap)):
        # Get random color for each circle
        tim.color(random_color())
        # Circle radius = 100
        tim.circle(100)
        # Tilt the turtle to the left
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)





# screen = Screen()
screen.exitonclick()

# Importing Modules in python (different ways)
# 1. Simple import: import turtle. This is convenient if the module is only being used once or twice.
# 2. from....import: from turtle import Turtle or from Turtle import *(as in everything in that module)
# 3. Aliasing module: import turtle as t

# Installing Modules --> use python package index or pypi to install external modules (or modules no preloaded with python)
