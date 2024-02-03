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


# Counterclockwise
def counter_clock():
    tim.setheading(45)


# Clockwise
def clockwise():
    tim.setheading(90)


screen.listen()


def move(key, *args):
    screen.onkey(key=key, fun=**kwargs)

    if key == "W":
        move_forward()
    elif key == "S":
        move_backward()
    elif key == "A":
        counter_clock()
    else:
        clockwise()


move("W")

screen.exitonclick()
