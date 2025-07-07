import random

def get_opponents_move():
    moveList = ["ROCK", "PAPER", "SCISSORS"]
    return moveList[random.randrange(0, len(moveList))]

def determine_outcome(your_choice, opponent_choice):
    # MOVE: THING IT BEATS
    moveDictionary = {
        "ROCK": "SCISSORS",
        "PAPER": "ROCK",
        "SCISSORS": "PAPER"
    }
    if(moveDictionary.get(your_choice) == opponent_choice):
        print(f"You win! {your_choice} beats {opponent_choice}!")
    elif(moveDictionary.get(opponent_choice) == your_choice):
        print(f"You lose! {opponent_choice} beats {your_choice}")
    else:
        print("It is a tie!")

def play(choice):
    opponent_move = get_opponents_move()
    match choice:
        case "ROCK":
            print(f"You chose ROCK and your opponent chose {opponent_move}!")
        case "PAPER":
            print(f"You chose PAPER and your opponent chose {opponent_move}!")
        case "SCISSORS":
            print(f"You chose SCISSORS and your opponent chose {opponent_move}!")
        case _: 
            print(f"You need to choose either ROCK, PAPER, or SCISSORS")
   
    determine_outcome(choice, opponent_move)

while True:
    if(input("Play game, Y or N: ").upper() == "N"):
        break

    choice = input("Choose either ROCK, PAPER, or SCISSORS: ")
    play(choice.upper())