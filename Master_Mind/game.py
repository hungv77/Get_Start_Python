import random

COLORS = ["A","B","C","D","E"]
TRIES = 10
CODE_LENGTH = 4

#Random ra một result
#Get answer from user
#Compare result
##Match colors and places
##Just match colors

# def generate_code():
#     code = []
#     for _ in range(CODE_LENGTH):
#         color = random.choice(COLORS)
#         code.append(color)
#     return code

def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code 

def guess_code():
    while True:
        #First, get the answer from the user
        guess = input("Guess: ").upper().split()
        #Check the condition, about Length and the Color
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue
        for color in guess:
            if color not in COLORS:
                print(f"Nuh uh, {color} that's not the color on the list. Try again.")
                break
        else: 
            break 
    return guess
        

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color]=0
        color_counts[color] += 1
    
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1
            
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1
            
    return correct_pos, incorrect_pos 

def game():
    print("Welcome to mastermind, you have {TRIES} to guess the code...")
    print("The valid colors are,", *COLORS)
    
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break 
            
        print(f"Correct Position: {correct_pos} | Incorrect Position: {incorrect_pos}")
        
    else:
        print("You ran out of tries, the code was:", *code)
            
if __name__ == "__main__":
    game()