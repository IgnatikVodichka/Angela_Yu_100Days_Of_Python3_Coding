from menu import MENU, resources
from coins import *


def is_resource_sufficient(drink_ingredients):
    """Returns 'True' when ingredients are sufficient, 'False' if ingredients are insufficient."""
    for item in drink_ingredients:

        if drink_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False

    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")

    total = int(input("how many quarters?: ")) * quarters
    total += int(input("how many dimes?: ")) * dimes
    total += int(input("how many nickles?: ")) * nickles
    total += int(input("how many pennies?: ")) * pennies

    return total


def is_transaction_successful(payment_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    global profit

    if payment_received >= drink_cost:
        change = round(payment_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, drink_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


profit = 0

is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}$")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()

            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
