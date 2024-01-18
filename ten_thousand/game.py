from game_logic import GameLogic


def play():
    # game variables
    round = 1
    total_score = 0
    dice_remaining = 6

    def roll_or_bank(kept_dice):
        nonlocal total_score
        nonlocal dice_remaining
        nonlocal round
        round_score = GameLogic.calculate_score(kept_dice)
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
            game_loop(dice_remaining)

    
    def game_loop(dice = 6):
        nonlocal dice_remaining
        print("Starting round ", round, "")
        GameLogic.roll_dice(dice)
        print("Enter dice to keep, or (q)uit: ")
        response = input(">")
        if response == "q":
            print("Thanks for playing. You earned 0 points")
            return
        else:
            kept_dice = list(response)
            kept_dice = [int(i) for i in kept_dice]
            dice_remaining = 6 - len(kept_dice)
            print("kept_dice: ", kept_dice)
            roll_or_bank(kept_dice)
    
    # welcome message
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    response = input(">")
    if response not in ["y", "n"]:
        print("Invalid response. Try again")
        play()
    if response == "n":
        print("OK. Maybe another time")
        return
    elif response == "y":
        game_loop()
    
  

    

if __name__ == "__main__":
    play()
