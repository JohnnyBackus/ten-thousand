from game_logic import GameLogic

# game variables
# dice_roller = roller or GameLogic.roll_dice
round = 1
total_score = 0
dice_remaining = 6

# welcome message
# def play(roller=None, num_rounds=10):
def play():    
    print("Welcome to Ten Thousand")
    start_menu()


def start_menu():
    print("(y)es to play or (n)o to decline")
    response = input(">")
    if response.lower() not in ["y", "yes", "n", "no"]:
        print("Invalid response. Try again")
        start_menu()
    if response == "n":
        print("OK. Maybe another time")
        return
    elif response == "y":
        game_loop()


def game_loop():
        global dice_remaining
        global round
        global total_score
        print("Starting round ", round, "")
        GameLogic.roll_dice(dice_remaining)
        print("Enter dice to keep, or (q)uit: ")
        response = input(">")
        if response == "q":
            print("Thanks for playing. You earned", total_score, "points")
            return
        else:
            kept_dice = list(response)
            kept_dice = [int(i) for i in kept_dice]
            dice_remaining -= len(kept_dice)
            # print("kept_dice: ", kept_dice)
            roll_or_bank(kept_dice)


def roll_or_bank(dice):
    global total_score
    global dice_remaining
    global round
    round_score = GameLogic.calculate_score(dice)
    total_score += round_score
    print("You have ", round_score, " unbanked points and ", dice_remaining, " dice remaining")
    print("(r)oll again, (b)ank your points or (q)uit: ")
    response = input(">")
    if response == "q":
        print("Thanks for playing. You earned ", total_score, " points")
        return
    elif response == "b":
        print("You banked ", round_score, " in round ", round, "")
        round += 1
        print("Total score is ", total_score, "points")
        game_loop()
    elif response == "r":
        game_loop()
    
      

if __name__ == "__main__":

    play()
    # rolls = [(3, 2, 5, 4, 3, 3),
    #          (5, 3, 3, 2, 1, 4),
    # ]
    
    # def mock_roller(num_dice):
    #     return [rolls.pop(0)]
    
    # play(roller=mock_roller)
