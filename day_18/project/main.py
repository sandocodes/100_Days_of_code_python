import turtle as t
import colorgram
import random

brush = t.Turtle()
screen = t.Screen()
t.colormode(255)

# Extract colors from image.jpg
color_list = []
colors = colorgram.extract('image.jpg', 50)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)


def random_color():
    return random.choice(color_list)


brush.setheading(199)
brush.forward(300)
brush.setheading(0)

for i in range(5):
    for _ in range(10):
        brush.dot(10, random_color())
        brush.forward(50)
        brush.dot(10, random_color())

    brush.setheading(90)
    brush.forward(50)
    brush.setheading(180)
    brush.forward(500)
    brush.setheading(0)




screen.exitonclick()
