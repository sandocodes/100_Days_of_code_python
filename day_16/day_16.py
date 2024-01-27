"""
Object-Oriented Programming (OOP)
- Two things to keep in mind when it comes to objects in OOP:
    1. What the object has (attributes)
    2. What the object does (methods)

    Example: waiter at a restaurant:
        Attributes: hold plates, responsible for tables, ect.
        Methods: take orders, take payments, etc.
"""
# Constructing Objects and Accessing their attributes and methods
# car = CarBluePrint()
# car is the Object and CarBluePrint is the Class

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# Object methods:

from prettytable import PrettyTable


table = PrettyTable()
table.add_column("Pokemon", ["Good", "Bad", "Ugly"])
table.add_column("Type", ["Good1", "Bad1", "Ugly1"])


print(table)
