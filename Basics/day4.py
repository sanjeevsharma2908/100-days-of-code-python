#paper scissors end game
# What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
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

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")
if user_choice == 0 and computer_choice ==2:
    print('You win!')
elif computer_choice == 0 and user_choice == 2:
    print('You lose!')
elif computer_choice > user_choice:
    print('You lose!')
elif user_choice > computer_choice:
    print('You win!')
elif computer_choice == user_choice:
    print('Its a draw')
elif user_choice >= 3:
    print('You typed an Invalid Number, you lose!')