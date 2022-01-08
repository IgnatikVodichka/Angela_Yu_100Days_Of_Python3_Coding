import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
is_end = True

print("Welcome to secret auction program")


def highest_bidder_checker(bidders):
    for name in bidders:
        max_bid = 0
        if bidders[name] > max_bid:
            max_bid = bidders[name]
            winner = name
    print(f"The highest bidder is {name} with bid {max_bid}")


while is_end:
    bidders = {input("Please enter your name: \n"): int(
        input("Please Enter your bid: \n"))}
    any_one_else = input("Are there any other bidders? Type 'yes' or 'no' ")

    if any_one_else == "no":
        is_end = False
        highest_bidder_checker(bidders)
    else:
        os.system("clear")


# print(max(bidders.values()))
