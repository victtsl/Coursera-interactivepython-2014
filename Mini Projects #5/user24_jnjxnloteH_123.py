# implementation of card game - Memory

import simplegui
import random
state = 0
numbers = []
#exposed = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
exposed = ["true","true","false","false","false","false","false","false","false","false","false","false","false","false","false","false"]

# helper function to initialize globals
def new_game():
    global numbers
    numbers = range(8) * 2
    #random.shuffle(numbers)
    print "Length", len(numbers), numbers
    print "Exposed", len(exposed), 
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed
    exposed[(pos[0]//50)] = "true"
    if state == 0:
        state = 1
        #print "exposed = ", exposed[(pos[0]//50)] = "true"
    elif state == 1:
        state = 2
    else:
        state = 1
    print "POS = ", pos 
    print pos[0] // 50
    #print "Exposed = ", exposed[n]
                        
# cards are logically 50x100 pixels in size    
def draw(c):
    global state, numbers, exposed
    #c.draw_line((0,0),(800,0),2,"white")
    #c.draw_line((0,0),(0,100),2,"white")
    #c.draw_line((0,100),(800,100),2,"white")
    #c.draw_line((0,100),(800,100),2,"white")
    for x in range(16):
        c.draw_polygon([(x * 50, 0), (x * 50, 100), ((x + 1) * 50, 100), ((x + 1) * 50, 0)], 1, 'White', 'Green')
        #print [(x * 50, 0), (x * 50, 100), ((x + 1) * 50, 100), ((x + 1) * 50, 0)]
    #c.draw_text(str(state) + " card exposed", [30, 62], 24, "White")
    #c.draw_text('1', [40 / 2, 60], 30, 'Red')
    x = 0
    for n in numbers:
        if exposed[x] == "true":
            #c.draw_text(str(n), [x * 50 / 2, 50], 30, 'Red')
            c.draw_text(str(n), [(x * 50) + 20, 60], 30, 'Red')
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