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
        # drink = ""
        # for item in Menu().menu:
        #     if item.name == choice:
        #         drink += item.name
        if CoffeeMaker().is_resource_sufficient(Menu().find_drink(choice)):
            # print(f"Enough Resources to get {choice}.")
            # Process Payment
            # Checking if payment is enough
            # MoneyMachine().process_coins()

            # Cost of desired item or specific item cost
            drink_cost = 0
            for item in Menu().menu:
                if item.name == choice:
                    drink_cost += item.cost
            print(f"{choice} costs ${drink_cost}")  # Test Purpose

            if MoneyMachine().make_payment(drink_cost):
                # Make Coffee and Print out result
                item_ordered = Menu().find_drink(choice)
                CoffeeMaker().make_coffee(item_ordered)

                # Add to profit
                change = round(MoneyMachine().money_received - drink_cost, 2)
                add_to_profit = MoneyMachine().money_received - change
                MoneyMachine().profit += add_to_profit
                print(f"{add_to_profit} added to Profit")  # Test Purpose
