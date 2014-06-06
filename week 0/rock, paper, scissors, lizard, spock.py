# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    if name == 'rock':
        name = 0
    elif name == 'paper':
        name = 1
    elif name == 'scissors':
        name = 2
    elif name == 'lizard':
        name = 3
    elif name == 'Spock':
        name = 4
    else:
        return "Error"
    return name


def number_to_name(number):
    if number == 0:
        number = 'rock'
    elif number == 1:
        number ='paper'
    elif number == 2:
        number = 'scissors'
    elif number == 3:
        number = 'lizard'
    elif number == 4:
        number = 'Spock'
    else:
        return 'Error'
    return number
    

def rpsls(player_choice): 
    print
    print 'Player chooses ' + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print 'Computer chooses ' + comp_choice
    # print out the message for computer's choice
    result = (comp_number - player_number) % 5
    # compute difference of comp_number and player_number modulo five
    if result == 2 or result == 1:
        print 'Computer wins'
    elif result == 3 or result == 4:
        print 'Player wins'
    else:
        print 'It\'s a tie'
    # use if/elif/else to determine winner, print winner message

    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

