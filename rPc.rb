#this is a simple rock paper scissors game for me to learn Ruby flow control and string manipulations
BEGIN{
	puts "Welcome to a simple Rock Paper Scissors simulator in Ruby"
}


choices = ["rock", "paper", "scissors"]
puts " Rock Paper or Scissors? Type in your Choice\n"

computer_choice =  choices.sample
user_choice = STDIN.gets.chomp.downcase ; puts " \n"
puts "You chose #{user_choice}\nComputer chose #{computer_choice}\n"; puts " \n"
bool = user_choice == computer_choice
#puts "#{bool}"

if user_choice == computer_choice
	puts "You chose #{user_choice} and the computer chose #{computer_choice} Looks like you are tied"
elsif (user_choice === "rock") && computer_choice == choices[1]
	puts "Paper beats Rock, Computer Wins"
elsif (user_choice === "rock") && computer_choice == choices[2]
	puts "Rock beats Scissors, You win"
elsif (user_choice === "paper") && computer_choice == choices[0]
	puts "Paper beats Rock, You Win"
elsif (user_choice === "paper") && computer_choice == choices[2]
	puts "Scissors beat paper, You lose"
elsif (user_choice === "scissors") && computer_choice == choices[1]
	puts "Scissors beat paper, You win"
elsif (user_choice === "scissors") && computer_choice == choices[0]
	puts "Rock beats Scissors, You lose"
else 
	puts "Please enter a valid choice"
end	
