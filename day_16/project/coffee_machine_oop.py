from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# is coffee machine on
is_machine_one = True

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
        # Get the drink order
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
