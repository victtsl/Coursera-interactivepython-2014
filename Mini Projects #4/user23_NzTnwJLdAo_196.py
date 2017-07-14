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
paddle1_pos = (HEIGHT / 2) - (PAD_HEIGHT / 2)
paddle2_pos = (HEIGHT / 2) - (PAD_HEIGHT / 2)
paddle1_vel = 0
paddle2_vel = 0

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
        ball_vel[0] = random.randrange(1, 10)
        ball_vel[1] = random.randrange(1, 10)
        #ball_vel = [3,3]
    if direction == LEFT:
        ball_vel[0] = random.randrange(-10, -1)
        ball_vel[1] = random.randrange(-10, -1)
        #ball_vel = [-3,-3]
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

    #Collision code
    #if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH):
    #if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) and (ball_pos[1] < paddle1_pos) and (ball_pos[1] > paddle1_pos + PAD_HEIGHT):
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) and ((ball_pos[1] < paddle1_pos) or (ball_pos[1] > paddle1_pos + PAD_HEIGHT)):
        #ball_vel[0] = - ball_vel[0]
        spawn_ball (RIGHT)
    elif (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) and (ball_pos[1] >= paddle1_pos) and (ball_pos[1] <= paddle1_pos + PAD_HEIGHT):
        ball_vel[0] = -ball_vel[0]
    #if ball_pos[0] >= (WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH):
    if (ball_pos[0] >= (WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH)) and ((ball_pos[1] < paddle2_pos) or (ball_pos[1] > paddle2_pos + PAD_HEIGHT)):
        #ball_vel[0] = - ball_vel[0]
        spawn_ball (LEFT)
    elif (ball_pos[0] >= (WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH)) and (ball_pos[1] >= paddle2_pos) and (ball_pos[1] <= paddle2_pos + PAD_HEIGHT):
        ball_vel[0] = -ball_vel[0]        
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]        
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]                
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos > 0 and (paddle1_pos + PAD_HEIGHT) < (HEIGHT - 1):
        paddle1_pos += paddle1_vel
    if paddle2_pos > 0 and (paddle2_pos + PAD_HEIGHT) < (HEIGHT - 1):
        paddle2_pos += paddle2_vel
    if (paddle1_pos <= 0 and (paddle1_vel > 0)) or ((paddle1_pos + PAD_HEIGHT) >= (HEIGHT -1) and (paddle1_vel < 0)):
        paddle1_pos += paddle1_vel
    if (paddle2_pos <= 0 and (paddle2_vel > 0)) or ((paddle2_pos + PAD_HEIGHT) >= (HEIGHT -1) and (paddle2_vel < 0)):    
        paddle2_pos += paddle2_vel
    #print "Paddle1 = ", paddle1_pos, "Paddle2 = ", paddle2_pos
    # draw paddles
    c.draw_line([0, paddle1_pos], [0, (paddle1_pos + PAD_HEIGHT)], PAD_WIDTH, 'Red')
    c.draw_line([(WIDTH -1), paddle2_pos], [(WIDTH - 1), (paddle2_pos + PAD_HEIGHT)], (PAD_WIDTH), 'Blue')
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 5
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 5
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 5
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 5        
            
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
        
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