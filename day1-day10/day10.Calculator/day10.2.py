import os
from art import logo
print(logo)


def multiplier(number1, number2):
    return number1 * number2


def divider(number1, number2):
    return number1 / number2


def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


operations = {"*": multiplier,
              "/": divider,
              "+": addition,
              "-": subtraction
              }


def calculator():
    number1 = float(input("Please enter first number: \n"))

    for operation in operations:
        print(operation)

    again = True

    while again:

        choose_operation = input("Please pick an operation: \n")
        number2 = float(input("Please input next number: \n"))
        calculation_function = operations[choose_operation]
        answer = calculation_function(number1, number2)

        print(f"{number1} {choose_operation} {number2} = {answer}")

        should_continue = input(
            f"Do you want to continue? type 'y' to continue with {answer} or type 'n' to start again: \n")
        if should_continue == 'y':
            number1 = answer
            continue
        elif should_continue == 'n':
            again = False
            os.system("clear")
            calculator()
        else:
            print("Invalid input")


calculator()
