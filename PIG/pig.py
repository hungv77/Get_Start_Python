import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# Nhập số lượng người chơi (2 - 4)
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break 
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again")
    
max_score = 50
player_scores = [0 for _ in range(players)]

# Bắt đầu game, chạy cho đến khi có người đạt max_score
while max(player_scores) < max_score:
  
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!\n")
        print("Your total score is:", player_scores[player_idx]) 
        current_score = 0
        
        # Vòng lặp trong lượt của người chơi
        while True:
            should_roll = input("Would you like to roll (y) or view score(v)? ").lower()
            
            # Người chơi muốn xem điểm của tất cả người chơi
            if should_roll == "v":
                for idx in range(players):
                    print("Player", idx + 1, "score is:", player_scores[idx])
                continue  # Sau khi xem điểm, quay lại hỏi có roll hay không
            
            # Người chơi không muốn roll nữa, thoát vòng lặp lượt của họ
            elif should_roll != "y":
                print("Ending your turn.\n")
                break

            # Xử lý việc lăn xúc xắc
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            
            print("Your score for this turn is:", current_score)
        
        # Cập nhật tổng điểm cho người chơi sau lượt chơi
        player_scores[player_idx] += current_score  # Đảm bảo luôn cộng điểm vào trước khi kết thúc
        print("Your total score is now:", player_scores[player_idx])
        
        # Kiểm tra nếu có người chơi đạt max_score
        if player_scores[player_idx] >= max_score:
            print("\nPlayer", player_idx + 1, "wins with a score of", player_scores[player_idx])
            break

