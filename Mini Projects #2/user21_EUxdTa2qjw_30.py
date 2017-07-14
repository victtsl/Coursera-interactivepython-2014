# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# initialize global variables used in your code
game_range = 100
number_guesses = 0
random_num = float(0.0)

# helper function to start and restart the game
def new_game():
    global random_num, number_guesses, game_range
    random_num = random.randint(0, int(game_range))
    if game_range == 100:
        number_guesses = 7
    else: number_guesses = 10
    print "New game. Range is", game_range
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global game_range, number_guesses
    game_range = float(100)
    number_guesses = 7
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global game_range
    game_range = float(1000)
    number_guesses = 10
    new_game()
    
def input_guess(guess):
    global game_range, random_num, number_guesses
    print "You guess ", guess
    number_guesses -= 1.0
    
    #if number_guesses == 0:
     #   print "Maximum guesses exceeded!", "\n", "\n"
      #  new_game()
        
    if float (guess) == float(random_num) and number_guesses != 0:
        print "Correct guess!", "\n", "\n"
        new_game()
    elif float (guess) > float(random_num) and number_guesses != 0:
        print "Lower"
    elif float (guess) < float(random_num) and number_guesses != 0:
        print "Higher"
    else:
        print "Maximum guesses exceeded!", "\n", "\n"
        new_game()
    print "number guesses", number_guesses
    
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