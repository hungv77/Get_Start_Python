print("Welcome to my computer quiz!")

playing = input("Do you want to play a game? ")

if playing.lower() != "yes":
  print("Ok bye?")
  quit()

print("Okay! Let's play, bitch: ")
score = 0

answer = input("Just say 1: ")
if answer.lower() == "1" :
  print('Correct!')
  score += 1
else:
  print("Incorrect!")
  
answer = input("Just say hi: ")
if answer.lower() == "hi" :
  print('Correct!')
  score += 1
else:
  print("Dumb bitch!")
  
answer = input("Just say 2: ")
if answer.lower() == "2" :
  print('Correct!')
  score += 1
else:
  print("Incorrect!")
  
print("You got " + str(score) + " questions correct!")