from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# instance of the Menu class
menu = Menu()
# instance of the CoffeeMaker class
coffee_maker = CoffeeMaker()
# instance of the MoneyMachine class
money_machine = MoneyMachine()

# is coffee machine on
is_machine_one = True

# while the coffee machine is still on
while is_machine_one:
    # user choice of drink (latte/espresso/cappuccino)
    choice = str(input(f"What would you like? ({menu.get_items()}): ")).lower()

    # if the user typed "off"
    if choice == "off":
        # Turn of the coffee machine
        is_machine_one = False
    # if the user typed "report"
    elif choice == "report":
        # print the report and the profit(money)
        coffee_maker.report()
        money_machine.report()
    # if the user typed anything else (latte/espresso/cappuccino)
    else:
        # Get the drink order of choice
        order = menu.find_drink(choice)

        # if there is sufficient resources of the order of choice and coin payment is sufficient
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            # Make the coffee
            coffee_maker.make_coffee(order)
