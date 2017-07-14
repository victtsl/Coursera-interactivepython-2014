# implementation of card game - Memory

import simplegui
import random
state = 0

# helper function to initialize globals
def new_game():
    

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state
    if state == 0:
        state = 1
    elif state == 1:
        state = 2
    else:
        state = 1
    
                        
# cards are logically 50x100 pixels in size    
def draw(c):
    global state    
    #c.draw_line((0,0),(800,0),2,"white")
    #c.draw_line((0,0),(0,100),2,"white")
    #c.draw_line((0,100),(800,100),2,"white")
    #c.draw_line((0,100),(800,100),2,"white")
    for x in range(16):
        c.draw_polygon([(x * 50, 0), (x * 50, 100), ((x + 1) * 50, 100), ((x + 1) * 50, 0)], 1, 'White', 'Green')
        #print [(x * 50, 0), (x * 50, 100), ((x + 1) * 50, 100), ((x + 1) * 50, 0)]
    c.draw_text(str(state) + " card exposed", [30, 62], 24, "White")
    #c.draw_polygon([(50, 0), (50, 100), (100, 100), (100, 0)], 1, 'White', 'Green')
    #c.draw_polygon([(100, 0), (100, 100), (150, 100), (150, 0)], 1, 'White', 'Green')
    #c.draw_polygon([(150, 0), (150, 100), (200, 100), (200, 0)], 1, 'White', 'Green')

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