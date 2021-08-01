import random
import os
from art import logo, vs
from game_data import data


def celebrity_selector():
    '''Choses 1 random celebrity'''
    choice = random.choice(data)
    return choice


def follower_compare_correct_answer(A, B):
    '''Compares followers from two random celebritites'''
    if A["follower_count"] > B["follower_count"]:
        return 'A'
    else:
        return 'B'


def game():

    game_over = False
    score = 0

    while not game_over:

        A = celebrity_selector()
        B = celebrity_selector()

        print(logo)

        print(
            f"Compare A: {A['name']}, {A['description']}, from: {A['country']}"
        )

        print(vs)

        print(
            f"Against B: {B['name']}, {B['description']}, from: {B['country']}"
        )

        user_answer = input("Who has more followers? 'A' or 'B': ")

        os.system("clear")

        if user_answer == follower_compare_correct_answer(A, B):
            print("Correct! You Guessed it!")
            score += 1
            print(f"Your current score: {score}")
        else:
            print("Nope!")
            print(f"Your final score: {score}")
            game_over = True


game()
