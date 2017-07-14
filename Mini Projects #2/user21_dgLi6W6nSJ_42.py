# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# initialize global variables used in your code
game_range = float(100)
number_guesses = float(0)
random_num = float(0)

# helper function to start and restart the game
def new_game():
    global random_num, number_guesses, game_range
    number_guesses = float(7)
    random_num = random.randint(0, int(game_range))
    print "New game. Range is ", game_range
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global game_range
    game_range = float(100)

def range1000():
    # button that changes range to range [0,1000) and restarts
    global game_range
    game_range = float(1000)
    
def input_guess(guess):
    global game_range, random_num
    print "You guess ", float(guess), float(random_num)
    if guess == random_num:
        print "Correct guess!"
    elif guess > random_num:
        print "Lower!"
    elif guess < random_num:
        print "Higher"       

    
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