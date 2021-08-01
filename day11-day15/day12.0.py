import random

attempts = 0
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randint(1, 100)

if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5

while attempts != 0:

    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number:
        print(f"You got it! The answer was {number}")
        exit(0)
    elif guess < number:
        print("Too low. \nGuess again.")
    elif guess > number:
        print("Too high. \nGuess again.")

    attempts -= 1


print("You've ran out of guesses, you lose.")
