import random

def chooser() :
    options = ["ROCK", "PAPER", "SCISSORS"]
    return random.choice(options)

def main():
    while True:
        print("All responses must be entered in all caps")
        opponent = input("Choose C for computer, L for a live opponent \n")

        if opponent in {"C", "c"}:
            userChoice = input("ROCK PAPER OR SCISSORS? \n")
            compChoice = chooser()
            if userChoice == compChoice:
                print("I choose {} and you chose {}. Guess we're tied \n".format(compChoice, userChoice))
            elif userChoice == "ROCK" and compChoice == "PAPER":
                print("I choose {} and you chose {}. Paper covers rock, I win \n".format(compChoice, userChoice))
            elif userChoice == "ROCK" and compChoice == "SCISSORS":
                print("I choose {} and you chose {}. Rock beats scissors, You win \n".format(compChoice, userChoice))
            elif userChoice == "SCISSORS" and compChoice == "PAPER":
                print("I choose {} and you chose {}. Scissors beat paper, you win \n".format(compChoice, userChoice))
            elif userChoice == "SCISSORS" and compChoice == "ROCK":
                print("I choose {} and you chose {}. Rock beat scissors, I win \n".format(compChoice, userChoice))
            elif userChoice == "PAPER" and compChoice == "ROCK":
                print("I choose {} and you chose {}. Paper covers rock, you win \n".format(compChoice, userChoice))
            elif userChoice == "PAPER" and compChoice == "SCISSORS":
                print("I choose {} and you chose {}. Scissors beat paper, I win \n".format(compChoice, userChoice))
            else:
                print("Enter a valid choice of either rock paper or scissors \n")

        elif opponent in {"l", "L"}: #a friend of mine asked me to make it multiplayer so I did
            user1 = input("Player 1, enter your choice \n")
            user2 = input("player 2, enter your choice\n")
            if user1 == user2:
                print("Player 1 choose {} and player 2 chose {}. Guess you're tied".format(user1, user2))
            elif user1 == "ROCK" and user2 == "PAPER":
                print("Player 1 choose {} and player 2 chose {}. Paper covers rock, Player 2 wins".format(user1, user2))
            elif user1 == "ROCK" and user2 == "SCISSORS":
                print(
                    "Player 1 choose {} and player 2 chose {}. Rock beats scissors, Player 1 wins".format(user1, user2))
            elif user1 == "SCISSORS" and user2 == "PAPER":
                print("Player 1 choose {} and player 2 chose {}. Scissors beats Paper, Player 1 wins".format(user1,
                                                                                                             user2))
            elif user1 == "SCISSORS" and user2 == "ROCK":
                print(
                    "Player 1 choose {} and player 2 chose {}. Rock beats scissors, Player 2 wins".format(user1, user2))
            elif user1 == "PAPER" and user2 == "ROCK":
                print("Player 1 choose {} and player 2 chose {}. Paper beats rock, Player 1 wins".format(user1, user2))
            elif user1 == "PAPER" and user2 == "SCISSORS":
                print("Player 1 choose {} and player 2 chose {}. Scissors beats paper, Player 2 wins".format(user1,
                                                                                                             user2))
            else:
                print("Enter a valid choice of either rock paper or scissors")
        else:
            print("Choose a valid opponent \n")

        exit = input("Exit Game? (y/n) \n")
        if exit in {"Y", "y"}:
            return

if __name__ == "__main__":
    main()