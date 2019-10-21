import random

def chooser() :
    options = ["ROCK", "PAPER", "SCISSORS"]
    return random.choice(options)

def main():
    userChoice = input("ROCK PAPER OR SCISSORS? \n")
    compChoice= chooser()
    if userChoice == compChoice :
        print ("I choose {} and you chose {}. Guess we're tied".format(compChoice, userChoice))
    elif userChoice == "ROCK" and compChoice == "PAPER":
        print ("I choose {} and you chose {}. Paper covers rock, I win".format(compChoice, userChoice))
    elif userChoice == "ROCK" and compChoice == "SCISSORS":
        print ("I choose {} and you chose {}. Rock beats scissors, You win".format(compChoice, userChoice))
    elif userChoice == "SCISSORS" and compChoice == "PAPER":
        print ("I choose {} and you chose {}. Scissors beat paper, you win".format(compChoice, userChoice))
    elif userChoice == "SCISSORS" and compChoice == "ROCK":
        print ("I choose {} and you chose {}. Rock beat scissors, I win".format(compChoice, userChoice))
    elif userChoice == "PAPER" and compChoice == "ROCK":
        print ("I choose {} and you chose {}. Paper covers rock, you win".format(compChoice, userChoice))
    elif userChoice == "PAPER" and compChoice == "SCISSORS":
        print ("I choose {} and you chose {}. Scissors beat paper, I win".format(compChoice, userChoice))
    else:
        print("Enter a valid choice of either rock paper or scissors")


if __name__ == "__main__":
    main()