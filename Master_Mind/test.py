import random

# B1: Making list random colors
colors = ['R', 'G', 'B', 'Y', 'O', 'P']  #All the colors that we can be use
answer = random.choices(colors, k=4)  #Combo 4 colors in game
print("Test answer:", answer)  #Debug

# B2: Loop Guessing
attempts = 0  #attempt

print("Hello, this is Mastermind Game!")
print("All Color: R (Red), G (Green), B (Blue), Y (Yellow), O (Orange), P (Purple).")
print("Let's guess 4 colors, ex: RGBY.")

while True:
    #B2: Player make their guess
    guess = input("What is your answer: ").strip().upper()
    attempts += 1  #Count

    #B3: Checking validity
    if len(guess) != 4 or not all(c in colors for c in guess):
        print("Nuh uh. Let's guess 4 colors in the list. Like RBGY or OPYY. Like that, eh?")
        continue

    #B4: Checking the answer
    exact_match = sum(a == g for a, g in zip(answer, guess))  #Right color, right place
    color_match = sum(min(answer.count(c), guess.count(c)) for c in set(guess)) - exact_match  #Right color, wrong place
    # B5: Print Result
    print(f"Bạn có {exact_match} màu đúng vị trí và {color_match} màu đúng nhưng sai vị trí.")

    #Win - Checking
    if exact_match == 4:
        print(f"Chúc mừng! Bạn đã đoán đúng mã đáp án: {''.join(answer)}")
        print(f"Bạn đã mất tổng cộng {attempts} lần đoán.")
        break
