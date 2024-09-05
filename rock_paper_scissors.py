import random 

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
options[0]

while True:
  user_input = input("Type Rock(R)/Paper(P)/Scissor(S) or Q to quit: ").lower()
  
  if user_input == "q":
    break
  
  if user_input not in ["rock", "paper", "scissor", "r", "p", "s"]:
    continue
  
  random_number = random.randint(0,2)
    #rock: 0, paper: 1, scissors: 2
  computer_pick = options[random_number]
  print("Computer picked", computer_pick + ".")
  
  if user_input in ["rock", "r"] and computer_pick == "scissor":
    print("You won!")
    user_wins += 1
    continue
    
  elif user_input in ["paper", "p"] and computer_pick == "rock":
    print("You won!")
    user_wins += 1
    continue
  
  elif user_input in ["scissor", "s"] and computer_pick == "paper":
    print("You won!")
    user_wins += 1
    continue
  
  else:
    print("You lose!")
    computer_wins += 1


print("Score - user: " + str(user_wins) + " - computer: " + str(computer_wins))
print("Goodbye?")