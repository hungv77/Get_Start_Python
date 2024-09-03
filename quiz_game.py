print("Welcome to my computer quiz!")

playing = input("Do you want to play a game? ")

if playing != "yes" and playing != "Yes":
  print("Ok bye?")
  quit()

print("Okay! Let's play, bitch: ")

answer = input("What does CPU stand for? ")

if answer == "Central Processing Unit" :
  print('Correct!')
else:
  print("Incorrect!")
  