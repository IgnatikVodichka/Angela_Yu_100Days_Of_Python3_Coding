import random
from art import logo, vs
from game_data import data


def follower_compare():
    if compare1["follower_count"] > compare2["follower_count"]:
        return True
    else:
        return False


compare1=random.choice(data)
compare2=random.choice(data)

correct_answer = follower_compare()

print(logo)

print(f"Compare A:{compare1["name"]}, {compare1["description"]}, from: {compare1["country"]}")

print(vs)


