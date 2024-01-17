from ten_thousand.game_logic import GameLogic

def play():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    response = input(">")
    if response == "n":
        print("OK. Maybe another time")
        return
    elif response == "y":
        print("Starting round 1")
        return
    else:
        print("Invalid response. Try again")
        play()





# play()

