import random

names = input("Please enter name separated by the coma.").split(",")

print(names)

print(f"{names[random.randint(0, len(names))]} is going to pay today")
