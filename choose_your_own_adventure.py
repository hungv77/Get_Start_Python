name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
  "You're on a dirt road, it has come to an end and you can go left or right."
).lower()

if answer == "left":
  answer = input(
    "You come to a river. You can walk or swim across?"
  )
  
  if answer == "swim":
    print()
  elif answer == "walk":
    print()
  else:
    print("Not a valid option. You lose.")
  
elif answer == "right":
  print()
else: 
  print("Not a valid option. You lose.")