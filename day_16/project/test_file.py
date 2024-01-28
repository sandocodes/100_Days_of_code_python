from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# machine_on = True

# while machine_on:
item = input("What would you like?: ")

# Cost of desired item or specific item cost
item_cost = 0
for i in Menu().menu:
    if i.name == item:
        item_cost += i.cost
        # print(i.name, i.cost)
print(f"{item} costs ${item_cost}")

#
if MoneyMachine().make_payment(item_cost):
    print("Payment made")
else:
    print("Insufficient funds")

# Checking if payment is enough
# MoneyMachine().process_coins()
# print(money_received)  # Money Received

# List items and their prices
# for i in Menu().menu:
#     print(f"{i.name}: {i.cost}")

# print(make_payment)
# 1. Get Order
item_order = Menu().find_drink(item)
print(f"{item_order}")

# Make Coffee
print(CoffeeMaker().make_coffee(item_order))

# 2. Update Money in Resources
# Change amount:
change = round(MoneyMachine().money_received - item_cost, 2)
amount_to_add = MoneyMachine().money_received - change
MoneyMachine().profit += amount_to_add
print(MoneyMachine().profit)
print(f"{amount_to_add} added to Profit")

# Update resources
resources = CoffeeMaker().resources
for i in resources:
    print(f"{resources}")

for item in item_order.ingredients:
    CoffeeMaker().resources[item] -= item_order.ingredients[item]
print(f"Here is your {item_order.name} ☕️. Enjoy!")

for i in resources:
    print(f"{resources}")

# Update Report

