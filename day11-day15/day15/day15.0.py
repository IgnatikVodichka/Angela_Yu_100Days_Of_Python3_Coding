from menu import MENU, resources
from coins import *


def report(money):
    '''Prints status report of coffee machine'''
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money}")


def resources_check(choice, money):
    '''Checks if enough resources'''
    if resources["water"] < MENU[choice]["ingredients"]["water"]:
        print("Not enough water")
        return False

    elif resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
        print("Not enough coffee")
        return False

    elif money < MENU[choice]["cost"]:
        print("You don't have enough money. Money refunded.")
        money = 0
        return False

    elif choice != "espresso":
        if resources["milk"] < MENU[choice]["ingredients"]["milk"]:
            print("Not enough milk")
            return False

    else:
        return True


def inserted_coins():
    '''Counts sum of money with quantity of inserted coins'''
    sum_of_pennies = int(
        input("Please insert quantity of pennies: ")) * pennies

    sum_of_nickles = int(
        input("Please insert quantity of nickles: ")) * nickles

    sum_of_dimes = int(input("Please insert quantity of dimes: ")) * dimes

    sum_of_quarters = int(
        input("Please insert quantity of quarters: ")) * quarters

    money = sum_of_pennies + sum_of_nickles + sum_of_dimes + sum_of_quarters

    return money


user_choice = input(
    "What would you like? (espresso / latte / cappuccino): ").lower()


if user_choice == "off":
    exit(0)

elif user_choice == "espresso":
    money = round(inserted_coins())
    order = resources_check(user_choice, money)
    if order == True:
        change = money - MENU[user_choice]["cost"]
        print(f"Here is your {user_choice} and money in change: {change}")

elif user_choice == "latte":
    money = round(inserted_coins())
    order = resources_check(user_choice, money)
    if order == True:
        change = money - MENU[user_choice]["cost"]
        print(f"Here is your {user_choice} and money in change: {change}")

elif user_choice == "cappuccino":
    money = round(inserted_coins())
    order = resources_check(user_choice, money)
    if order == True:
        change = money - MENU[user_choice]["cost"]
        print(f"Here is your {user_choice} and money in change: {change}")
