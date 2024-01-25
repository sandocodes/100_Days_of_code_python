# Testing
import data

resources = {
    "water": 100,
    "milk": 200,
    "coffee": 100,
}
user_input = input("Enter an item: ")
order_ingredients = data.MENU[user_input]["ingredients"]
is_sufficient = True
for item in order_ingredients:
    if order_ingredients[item] >= resources[item]:
        print(f"Sorry there is not enough {item}")
        is_sufficient = False




