"""
<<<<<<< Updated upstream
Coffee Machine Object-Oriented Version
=======
Building Coffee Machine from Day_15 using Object-Oriented Programming (OOP)
>>>>>>> Stashed changes
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_machine_on = True
while is_machine_on:
    choice = input(f" What would you like? Type ({menu.get_items()}): ").lower()
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        report = coffee_maker.report()
        money = money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # Check if there's sufficient resources of item ordered and the payment is sufficient(accepted)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
