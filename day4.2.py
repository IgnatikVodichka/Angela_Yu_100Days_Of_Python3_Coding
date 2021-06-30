import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


weapons = [rock, paper, scissors]

computer_choice = weapons[random.randint(0, 2)]

player_choice = weapons[int(input(
    "Weapon of choice: 0 for rock, 1 for paper and 2 for scissors\nWhat will you choose: "))]

print(f"Your choice:\n{player_choice}")
print(f"Computer chose:\n{computer_choice}")

if computer_choice == player_choice:
    print("That's a tie")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and player_choice == 2:
    print("You lose")
elif computer_choice > player_choice:
    print("You lose")
elif player_choice > computer_choice:
    print("You win!")
