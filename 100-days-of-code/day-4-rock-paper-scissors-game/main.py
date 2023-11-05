import random

# Rock, Paper, Scissors Game

#Used: list[], random.randint(), if:/elif:, print(), input(), int() and quit()

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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice > 2 or user_choice < 0:
    print("You have entered an invalid choice. Please try again.")
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice > 2 or user_choice < 0:
        print("Invalid choice again. You lose.")
        quit()
        
print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("Somehow you typed a invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win! Rock beats scissors.")
elif computer_choice == 0 and user_choice == 2:
    print("You lose. Rock beats scissors.")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print(f"It's a tie! You both chose:\n{game_images[user_choice]}")
    
quit()