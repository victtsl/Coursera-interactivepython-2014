# implementation of card game - Memory

import simplegui
import random
state = 0
numbers = []
first_pos = 0 
second_pos = 0
turns = 0
#exposed = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#exposed = ["false","false","false","false","false","false","false","false","false","false","false","false","false","false","false","false"]
exposed = [False] * 16
paired = [False] * 16

# helper function to initialize globals
def new_game():
    global numbers, exposed, state, exposed, paired, turns
    state = 0
    turns = 0
    numbers = range(8) * 2
    random.shuffle(numbers)
    #exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    exposed = [False] * 16
    paired = [False] * 16
    print "Len of numbers", len(numbers), numbers
    print "New Game State = ", state
    #print exposed
    label.set_text("Turns = " + str(turns))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global numbers, state, exposed, first_pos, second_pos, paired, turns
    #if (exposed[(pos[0]//50)] == False):
    if state == 0:
        first_pos = (pos[0]//50)
        #exposed[first_pos] = True
        print "Paired1 =", paired[first_pos], " Exposed1 =", exposed[first_pos]
        if not paired[first_pos] and not exposed[first_pos]:
            exposed[first_pos] = True
            state = 1
            turns += 1
        else:
            state = 0
        #print "exposed = ", exposed[(pos[0]//50)] = "true"
        
    elif state == 1:
        second_pos = (pos[0]//50)

        print "Paired2 =", second_pos, paired[second_pos], " Exposed2 =", exposed[second_pos]
        if not paired[second_pos] and not exposed[second_pos]:
            exposed[second_pos] = True
            state = 2
            turns += 1
        else:
            state = 1
        #if paired[first_pos] !=True:
        #    state = 2
        #elif paired[second_pos] != True:
        #    state = 2

    else:
        print "else state 3"
        state = 1
        turns += 1        
        third_pos = (pos[0]//50)
        #if (numbers[first_pos] != numbers[second_pos]) and not paired[first_pos] and not paired[second_pos]:
        if (numbers[first_pos] != numbers[second_pos]):
            if (not paired[first_pos]):
                print "close"
                exposed[first_pos] = False
                exposed[second_pos] = False
                if (exposed[third_pos]):
                    state = 0
        else:
            print "Found Pair!!!",
            paired[first_pos] = True
            paired[second_pos] = True
            print numbers[first_pos], " = ", numbers[second_pos]
            if paired[third_pos] and exposed[third_pos]:
                exposed[first_pos] = True
                state = 0
                #turns += 1
            
            #print "paired[0] = ", paired[0]
        #if numbers[first_pos] == "true"
        first_pos = (pos[0]//50)
        exposed[first_pos] = True
    print "state = ", state, "pos = ", pos[0]//50
    label.set_text("Turns = " + str(turns))
    #print "Exposed = ", exposed
    #print "POS = ", pos 
    #print pos[0] // 50
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
        if exposed[x] == True:
            #c.draw_text(str(n), [x * 50 / 2, 50], 30, 'Red')
            c.draw_text(str(n), [(x * 50) + 5, 80], 80, 'Red')
        x += 1
    
# create frame and add a button and labels
#global turns
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")
#print "Turns = ", turns
#label.set_text("Label = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric