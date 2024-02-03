# Turtle Event Listeners

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# right(0) - east --> counterclock
#


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


# Counterclockwise OR LEFTWARD
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


# Clockwise OR RIGHTWARD
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


# Clear Screen
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
