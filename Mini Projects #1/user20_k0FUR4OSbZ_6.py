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

def number_to_name(number):
    # fill in your code below
    if number == 0: 
        return "rock"
    elif number == 1: 
        return "Spock"
    elif number == 2: 
        return "paper"
    elif number == 3: 
        return "lizard"
    elif number == 4: 
        return "scissors"
    else: 
        return "Error number_to_name(number)"
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    if name == "rock":
        return 0
    if name == "Spock":
        return 1    
    if name == "paper":
        return 2
    if name == "lizzard":
        return 3
    if name == "scissors":
        return 4
    else: 
        return "Error name_to_number(name)"
    # convert name to number using if/elif/else
    # don't forget to return the result!
    #return "Test name_to_number(name)"

def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number

    # compute random guess for comp_number using random.randrange()

    # compute difference of player_number and comp_number modulo five

    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results
    print "Test rpsls(name)"
    
# test your code
print number_to_name(5)
print name_to_number("Spock")
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


