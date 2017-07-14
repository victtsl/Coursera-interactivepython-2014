# implementation of card game - Memory

import simplegui
import random
state = 0
numbers = []
first_pos = 0 
second_pos = 0
turns = 0
exposed = [False] * 16
paired = [False] * 16

# helper function to initialize globals
def new_game():
    global numbers, exposed, state, exposed, paired, turns
    state = 0
    turns = 0
    numbers = range(8) * 2
    random.shuffle(numbers)
    exposed = [False] * 16
    paired = [False] * 16
    #print "Numbers list", numbers
    #print "New Game State = ", state
    label.set_text("Turns = " + str(turns))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global numbers, state, exposed, first_pos, second_pos, paired, turns
    #At state 0, when you clicked on a card, determines if the card has been previously exposed and paired.
    #If not previously exposed and paired, expose the card and switch to state 1.
    #If the card has been previously exposed or paired, ignore mouseclick and remain at state 0.
    if state == 0:
        first_pos = (pos[0]//50)
        #print "Paired1 =", paired[first_pos], " Exposed1 =", exposed[first_pos]
        if not paired[first_pos] and not exposed[first_pos]:
            exposed[first_pos] = True
            state = 1
            turns += 1
        else:
            state = 0
    #At state 1, when you clicked on a card, determines if the card has been previously exposed and paired.
    #If not previously exposed and paired, expose the card and switch to state 2.
    #If the card has been previously exposed or paired, ignore mouseclick and remain at state 1.
    elif state == 1:
        second_pos = (pos[0]//50)
        #print "Paired2 =", second_pos, paired[second_pos], " Exposed2 =", exposed[second_pos]
        if not paired[second_pos] and not exposed[second_pos]:
            exposed[second_pos] = True
            state = 2
            turns += 1
        else:
            state = 1
    #At state 2, if clicked on a card that was previously unexposed, switch to state 1 and expose the card.
    #Determines if the 2 cards are paired, if they are not paired, flip them back and switch to state 1.
    #Otherwise keep both cards exposed.
    else:
        state = 1
        turns += 1        
        third_pos = (pos[0]//50)

        if (numbers[first_pos] != numbers[second_pos]):
            if (not paired[first_pos]):
                exposed[first_pos] = False
                exposed[second_pos] = False
                #If click on a card that was previously exposed, move to state 0
                if (exposed[third_pos]):
                    state = 0
        #If both cards are paired, keep then exposed.
        else:
            paired[first_pos] = True
            paired[second_pos] = True
            #If current card is already paired and exposed, change to state 0.
            if paired[third_pos] and exposed[third_pos]:
                exposed[first_pos] = True
                state = 0
                turns -= 1
        first_pos = (pos[0]//50)
        exposed[first_pos] = True
    #print "state = ", state, "pos = ", pos[0]//50
    label.set_text("Turns = " + str(turns))
                        
# cards are logically 50x100 pixels in size    
def draw(c):
    global state, numbers, exposed
    for x in range(16):
        c.draw_polygon([(x * 50, 0), (x * 50, 100), ((x + 1) * 50, 100), ((x + 1) * 50, 0)], 1, 'White', 'Purple')
    x = 0
    for n in numbers:
        if exposed[x] == True:
            c.draw_polygon([(x * 50, 0), (x * 50, 100), ((x + 1) * 50, 100), ((x + 1) * 50, 0)], 1, 'White', 'Black')
            c.draw_text(str(n), [(x * 50) + 5, 80], 80, 'Red')
        x += 1
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric