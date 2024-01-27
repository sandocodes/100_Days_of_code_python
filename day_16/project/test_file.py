from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

item = input("What would you like?: ")

item_cost = 0
for i in Menu().menu:
    item_cost += i.cost
print(item_cost)

# Specific item cost
for i in Menu().menu:
    if i.name == item:
        print(i.name, i.cost)

# Checking if payment is enough
money_received = MoneyMachine().process_coins()
print(money_received)