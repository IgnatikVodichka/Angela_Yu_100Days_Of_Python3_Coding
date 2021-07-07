import random

word_list = ["baboon", "camel", "cat", "dog"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = ["_"]*len(chosen_word)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
game_over = False
print(stages[-1])

while not game_over:
    guess = input("Please guss a letter: ").lower()
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
