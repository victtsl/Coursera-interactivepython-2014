# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# initialize global variables used in your code
game_range = 100
guesses_remain = 0
random_num = float(0.0)

# helper function to start and restart the game
def new_game():
    global random_num, guesses_remain, game_range
    random_num = random.randint(0, game_range)
    if game_range == 100:
        guesses_remain = 7
    else: guesses_remain = 10
    print "New game. Range is 0 to", game_range
    print "Number of remaining guesses:", guesses_remain, "\n"
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global game_range, guesses_remain
    game_range = 100
    guesses_remain = 7
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global game_range
    game_range = 1000
    guesses_remain = 10
    new_game()
    
def input_guess(guess):
    global game_range, random_num, guesses_remain
    guesses_remain -= 1
    
    print "Number of remaining guesses:", guesses_remain
    print "You guess ", guess
    
    if float (guess) == float(random_num):
        print "Correct guess!", "\n", "\n"
        new_game()
    elif float (guess) > float(random_num) and guesses_remain != 0:
        print "Lower!\n"
    elif float (guess) < float(random_num) and guesses_remain != 0:
        print "Higher!\n"
    else:
        print "Maximum guesses exceeded! The number is", random_num, ".", "\n"
        new_game()

# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0, 100)",range100,200)
f.add_button("Range is [0, 1000)",range1000,200)
f.add_input("Enter a guess",input_guess,200)

# call new_game and start frame
f.start()
new_game()

# always remember to check your completed program against the grading rubric