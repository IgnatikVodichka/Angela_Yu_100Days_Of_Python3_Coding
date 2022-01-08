import random
import hangman_art
import hangman_words

from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
print(chosen_word)

display = ["_"]*len(chosen_word)

print(logo)
print(stages[-1])

lives = 6
game_over = False


while not game_over:
    guess = input("Please guess a letter: ").lower()
    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if guess == letter:
            display[index] = letter
    if guess not in chosen_word:
        print("Wrong letter")
        print(stages[lives-1])
        lives -= 1
    if lives == 0:
        print("You lost!")
        game_over = True
    print(display)
    if "_" not in display:
        game_over = True
        print("You won!")
