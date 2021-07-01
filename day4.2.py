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

computer_choice = random.randint(0, 2)

player_choice = int(input(
    "Weapon of choice: 0 for rock, 1 for paper and 2 for scissors\nWhat will you choose: "))

print(f"Your choice:\n{weapons[player_choice]}")
print(f"Computer chose:\n{weapons[computer_choice]}")

if computer_choice == player_choice:
    print("That's a tie")
elif computer_choice == 0 and player_choice == 1 or computer_choice == 1 and player_choice == 2 or computer_choice == 2 and player_choice == 0:
    print("You win!")
else:
    print("Computer wins!")
