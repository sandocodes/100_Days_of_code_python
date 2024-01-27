"""
Coffee Machine Object-Oriented Version
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
while machine_on:
    choice = input(f" What would you like? Type ({Menu().get_items()}): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        report = CoffeeMaker().report()
        money = MoneyMachine().report()
        # print(report)
    else:
        # print(CoffeeMaker().is_resource_sufficient(Menu().find_drink(choice)))  # True
        # Check if item is sufficient
        if CoffeeMaker().is_resource_sufficient(Menu().find_drink(choice)):

            print(f"Enough Resources to get {choice}.")
            # Process Payment
            # Have enough money ?

        else:
            print(f"Not Enough Resources to Get {choice}.")
