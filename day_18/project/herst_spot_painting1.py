import turtle as t
import colorgram
import random

brush = t.Turtle()
screen = t.Screen()
t.colormode(255)

# Extract 40 colors from Image
rgb_colors = []
colors = colorgram.extract('image.jpg', 40)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


# Random Color from the color list
def get_random_color():
    random_color = random.choice(rgb_colors)
    return random_color


# Create dots
print(brush.setheading())







screen.exitonclick()
