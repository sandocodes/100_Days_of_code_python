"""
    Project:
    Written by:
    Description:
    Date:
    Project source:
"""

import data


# Update or Change report each time an item is bought
def update_report(item_bought, amt):
    for i in data.MENU[item_bought]["ingredients"]:
        # new balances
        data.resources[i] -= data.MENU[item_bought]["ingredients"][i]
    # Add money to resources
    if "money" in data.resources:
        data.resources["money"] += amt
    else:
        data.resources["money"] = amt


def brew(item, amt):
    """Calculate latte price"""
    if amt < data.MENU[item]["cost"]:
        # make coffee
        print("Sorry that's not enough money. {amt} refunded")
    elif amt > data.MENU[item]["cost"]:
        # Check if we still have the items the user requested
        change = round(float(amt - data.MENU[item]["cost"]), 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {item} ☕️. Enjoy!")
        update_report(item, amt - change)
    else:
        change = round(float(amt - data.MENU[item]["cost"]), 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {item} ☕️. Enjoy!")
        update_report(item, amt - change)


machine_on = True
while machine_on:
    user_input = str(input(" What would you like? (espresso/latte/cappuccino): "))

    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        if (user_input == "espresso" and (data.resources["water"] < 50 or data.resources["coffee"] < 18)) or (
                user_input == "latte" and (
                data.resources["water"] < 200 or data.resources["milk"] < 150 or data.resources["coffee"] < 24)) or (
                user_input == "cappuccino" and (
                data.resources["water"] < 200 or data.resources["milk"] < 100 or data.resources["coffee"] < 24)):
            print(f"Sorry, we're out of {user_input}")
        else:
            print("Please insert coins.")
            quarters = float(input("how many quarters: ")) * 0.25
            dimes = float(input("how many dimes: ")) * 0.1
            nickles = float(input("how many nickles: ")) * 0.05
            pennies = float(input("how many pennies: ")) * 0.01

            coins_total = float(quarters + dimes + nickles + pennies)

            brew(user_input, coins_total)

    elif user_input == "report":
        # Display Report
        water = data.resources["water"]
        milk = data.resources["milk"]
        coffee = data.resources["coffee"]
        if "money" not in data.resources:
            data.resources["money"] = 0
        money = data.resources["money"]

        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

    elif user_input == "off":
        machine_on = False
    else:
        print("Invalid input")
