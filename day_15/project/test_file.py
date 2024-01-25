# Testing
import data
user_input = input("Enter an item: ")
order_ingredients = data.MENU[user_input]["ingredients"]

for item in order_ingredients:
    if item in order_ingredients[item] >= data.resources[item]:
        print(f"Sorry there is not enough {item}")
        return False
return True



