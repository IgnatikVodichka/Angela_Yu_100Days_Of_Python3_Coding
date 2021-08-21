from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    choice = input(f"​What would you like? {menu.get_items()}: ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        machine.report()
        money_machine.report()

    # elif machine.is_resource_sufficient(menu.find_drink(choice)) == True:
    #     money_machine.make_payment()
