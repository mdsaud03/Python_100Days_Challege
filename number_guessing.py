import random

print("""
                           _   _                                _               
                          | | | |                              | |              
  __ _ _   _  ___  ___ ___| |_| |__   ___ _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / _` | | | |/ _ \/ __/ __| __| '_ \ / _ \ '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| (_| | |_| |  __/\__ \__ \ |_| | | |  __/ | | | |_| | | | | | | |_) |  __/ |   
 \__, |\__,_|\___||___/___/\__|_| |_|\___|_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
  __/ |                                                                         
 |___/                                                                          
""")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_ans(usr_guess, actual_answer, turns):
    if usr_guess > actual_answer:
        print("Too High")
        return turns - 1
    elif usr_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You win!!! The answer is {actual_answer}")
        return 0  # Player has won, return 0 turns


def difficulty():
    level = input("Enter your difficulty level (easy/hard): ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} turns left.")
        guess = int(input("Make a guess: "))
        turns = check_ans(guess, answer, turns)

        if turns == 0:
            break

    if turns == 0 and guess != answer:
        print(f"You lose! The correct answer was {answer}")


game()
