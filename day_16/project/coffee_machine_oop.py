from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# is coffee machine on
is_machine_one = True

while is_machine_one:
    choice = str(input(f"What would you like? ({menu.get_items()}): ")).lower()
    if choice == "off":
        is_machine_one = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
