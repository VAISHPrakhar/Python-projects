import random

def rock_paper_scissors():
  choices = ["rock", "paper", "scissors"]
  user_choice = input("Enter rock, paper, or scissors: ")
  computer_choice = random.choice(choices)
  
  if user_choice == computer_choice:
      return "It's a tie!"
  elif user_choice == "rock":
      return "You win!" if computer_choice == "scissors" else "You lose!"
  elif user_choice == "paper":
      return "You win!" if computer_choice == "rock" else "You lose!"
  elif user_choice == "scissors":
      return "You win!" if computer_choice == "paper" else "You lose!"

print(rock_paper_scissors())