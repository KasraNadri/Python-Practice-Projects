import random
import time

prompt = input("What do you choose? Rock, Paper or Scissors?\n").strip().lower()

computer_choices = ["rock", "paper", "scissors"]

computer_choice = random.choice(computer_choices)

print("...")

time.sleep(1)

print(f"Computer chose {computer_choice}!")

if computer_choice == "rock" and prompt == "rock" or computer_choice == "paper" and prompt == "paper" or computer_choice == "scissors" and prompt == "scissors":
  print("It's a tie!")
  
elif computer_choice == "rock" and prompt == "scissors" or computer_choice == "scissors" and prompt == "paper" or computer_choice == "paper" and prompt == "rock":
  print("You win!")
  
elif computer_choice == "scissors" and prompt == "rock" or computer_choice == "paper" and prompt == "scissors" or computer_choice == "rock" and prompt == "paper":
  print("Computer wins!")
  
else:
  print("Invalid input. Please try again.")
  