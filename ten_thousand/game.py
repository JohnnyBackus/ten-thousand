from game_logic import GameLogic

# game variables
# dice_roller = roller or GameLogic.roll_dice
round = 1
round_score = 0
game_score = 0
dice_remaining = 6


def play(): # welcome message and starts game
    print("Welcome to Ten Thousand")
    start_menu()


def start_menu(): #separated from welcome message to not repeat welcome in event of invalid response
    print("(y)es to play or (n)o to decline")
    response = input(">")
    if response.lower() not in ["y", "yes", "n", "no"]:
        print("Invalid response. Try again")
        start_menu()
    if response == "n":
        print("OK. Maybe another time")
        return
    elif response == "y":
        start_round_message()


def start_round_message():
    global round
    print("Starting round", round, "")
    game_loop()


def quit_game():
    global game_score
    print("Thanks for playing. You earned ", game_score, " points")
    return


def play_another_round():
    print("Play another round? (y)es or (n)o")
    response = input(">")
    if response.lower() not in ["y", "yes", "n", "no"]:
        print("Invalid response. Try again")
        play_another_round()
    if response == "y":
        start_round_message()
    if response == "n":
        quit_game()


def zilch():
    global round
    global dice_remaining
    global game_score
    print("""
            ****************************************
            **        Zilch!!! Round over         **
            ****************************************
            """)
    print("You banked 0 points in round", round,"")
    print("Total score is", game_score, "points")
    round += 1 # increment round
    dice_remaining = 6 # reset dice remaining for next round
    play_another_round()
    

# def game_loop(roller=None, num_rounds=10):
def game_loop(): # game loop to handle each dice roll
    global dice_remaining
    if dice_remaining == 0:
        dice_remaining = 6 # hot dice situation, reset dice remaining for next roll
    # I am pleasantly shocked that the line below didn't break something!
    max_roll_score = GameLogic.calculate_score(GameLogic.roll_dice(dice_remaining))
    # print("max_round_score: ", max_round_score)
    if max_roll_score == 0:
        zilch()
    print("Enter dice to keep, or (q)uit: ")
    response = input(">")
    if response == "q":
        quit_game()
    else:
        kept_dice = list(response)
        kept_dice = [int(i) for i in kept_dice] 
        dice_remaining -= len(kept_dice)
        # print("kept_dice: ", type(kept_dice), kept_dice)
        roll_or_bank(kept_dice)


def bank():
    global game_score
    global round_score
    global dice_remaining
    global round
    game_score += round_score # add round score to game score
    print("You banked", round_score, "points in round", round, "")
    print("Your total score is", game_score, "points")
    round += 1 # increment round
    dice_remaining = 6 #reset dice remaining for next round
    start_round_message()


def roll_or_bank(dice): # roll or bank to handle scores and user choice
    global game_score
    global round_score
    global dice_remaining
    global round
    roll_score = GameLogic.calculate_score(dice)
    print("roll_score: ", roll_score)
    round_score += roll_score # add points from this roll to round score
    print("You scored", roll_score, "points this roll and have", round_score, "unbanked points this round with", dice_remaining, "dice remaining")
    print("(r)oll again, (b)ank your points or (q)uit: ")
    response = input(">")
    if response == "q":
        print("Thanks for playing. You earned", game_score, "points")
        return
    elif response == "b":
        bank()
    elif response == "r":
        game_loop()



if __name__ == "__main__":

    play()

    # rolls = [(3, 2, 5, 4, 3, 3),
    #          (5, 3, 3, 2, 1, 4),
    # ]
    
    # def mock_roller(num_dice):
    #     return [rolls.pop(0)]
    
    # game_loop(roller=mock_roller)

    # print("test calc_score", GameLogic.calculate_score([4, 2, 6]))
