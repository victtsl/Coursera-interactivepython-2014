# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
#init_pos = [WIDTH / 2, HEIGHT / 2]
time = 0
ball_vel = [0, 0]
ball_pos = [WIDTH / 2, HEIGHT / 2]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [WIDTH / 2, HEIGHT / 2]
    #ball_vel = [3,3]
    #ball_pos[0] += ball_vel[0]
    #ball_pos[1] += ball_vel[1]
    #ball_pos[0] = init_pos[0] + time * ball_vel[0]
    #ball_pos[1] = init_pos[1] + time * ball_vel[1]    

    if direction == RIGHT:
        ball_vel[0] = random.randrange(1, 50)
        ball_vel[1] = random.randrange(1, 50)
    if direction == LEFT:
        ball_vel[0] = random.randrange(-50, -1)
        ball_vel[1] = random.randrange(-50, -1)
    #print "Ball_vel = ", ball_vel
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    spawn_ball(LEFT)

def tick():
    global time
    time += 1    
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    #ball_pos = [0, 0]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        #ball_vel[0] = - ball_vel[0]
        spawn_ball (RIGHT)
    if ball_pos[0] >= (WIDTH - 1) - BALL_RADIUS:
        #ball_vel[0] = - ball_vel[0]
        spawn_ball (LEFT)
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]        
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]                
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# register event handlers
timer = simplegui.create_timer(100, tick)

# start frame
new_game()
frame.start()
timer.start()