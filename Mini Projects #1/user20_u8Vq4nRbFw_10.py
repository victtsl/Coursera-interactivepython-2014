# Rock-paper-scissors-lizard-Spock 
# Date: 10/20/2013

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
    player_number = name_to_number(name)
    comp_number = random.randrange(0,5)
        
    var1 = (comp_number - player_number) % 5
   
    print "Player chooses", name
    print "Computer chooses", number_to_name(comp_number)
    
    if var1 == 0:
        print "Player and computer tie!"
    elif var1 == 1 or var1 == 2:
        print "Computer wins!"
    else:
        print "Player wins!"
    print "\n"

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
