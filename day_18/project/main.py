import turtle as t
from colors import RandomColors

random_colors = RandomColors()

brush = t.Turtle()
brush.speed("fastest")
brush.penup()
brush.hideturtle()
screen = t.Screen()
t.colormode(255)


# Draw a (10 X 10) Painting with Random Colors
def _painting_dots():
    brush.setheading(225)
    brush.forward(300)
    brush.setheading(0)
    num_of_dots = 100

    for dot_count in range(1, num_of_dots + 1):
        brush.dot(20, random_colors.get_color())
        brush.forward(50)

        if dot_count % 10 == 0:
            brush.setheading(90)
            brush.forward(50)
            brush.setheading(180)
            brush.forward(500)
            brush.setheading(0)


_painting_dots()

screen.exitonclick()
