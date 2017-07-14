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
    #convert number to name
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
    
def name_to_number(name):
    #convert name to number
    if name == "rock":
        return int ('0')
    if name == "Spock":
        return int ('1')
    if name == "paper":
        return int ('2')
    if name == "lizard":
        return int ('3')
    if name == "scissors":
        return int ('4')
    else: 
        return "Error name_to_number(name)"

def rpsls(name): 
    import random
    # fill in your code below
    # convert name to player_number using name_to_number
    # compute random guess for comp_number using random.randrange()
    # compute difference of player_number and comp_number modulo five
    # use if/elif/else to determine winner
    # convert comp_number to name using number_to_name
    # print results

    player_number = name_to_number(name) + 1
        
    comp_number = random.randrange(0,5)
    #print random.randrange(0,5)
    
    var1 = comp_number % player_number
    var2 =  comp_number - player_number
    print "Player chooses", name
    print "Computer chooses", number_to_name(comp_number), comp_number
    
    print "Vars = ", var1, var2
    if var2 == -1:
        print "Draw!"
    elif var1 <= var2:
        print "Player wins!"
    elif var1 >= var2:
        print "Computer wins!"

    
    print "\n"
# test your code

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


