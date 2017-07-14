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
left_score = 0         
right_score = 0
    
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [WIDTH / 2, HEIGHT / 2]

    if direction == RIGHT:
        ball_vel[0] = random.randrange(1, 10)
        ball_vel[1] = random.randrange(1, 10)
    if direction == LEFT:
        ball_vel[0] = random.randrange(-10, -1)
        ball_vel[1] = random.randrange(-10, -1)
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global left_score, right_score  # these are ints
    left_score = 0         
    right_score = 0    
    
    if (random.randrange(1, 10) % 2) == 0:
        spawn_ball(LEFT)
    else:
        spawn_ball(RIGHT)        
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, left_score, right_score

    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_text(str(left_score), (140, 40), 32, 'Red')
    c.draw_text(str(right_score), (450, 40), 32, 'Blue')
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    #Collision code
    #if ball touches with LEFT gutter, spawn ball toward RIGHT gutter
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) and ((ball_pos[1] < paddle1_pos) or (ball_pos[1] > paddle1_pos + PAD_HEIGHT)):
        spawn_ball (RIGHT)
        right_score += 1

    #else if ball strikes LEFT paddle when touching the gutter, ball is reflected back into play
    #velocity of ball increased 10% everytime it strikes a paddle
    elif (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) and (ball_pos[1] >= paddle1_pos) and (ball_pos[1] <= paddle1_pos + PAD_HEIGHT):
        ball_vel[0] = -ball_vel[0] * 1.1

        #if ball touches with RIGHT gutter, spawn ball toward LEFT gutter        
    if (ball_pos[0] >= (WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH)) and ((ball_pos[1] < paddle2_pos) or (ball_pos[1] > paddle2_pos + PAD_HEIGHT)):
        spawn_ball (LEFT)
        left_score += 1        
    #else if ball strikes RIGHT paddle when touching the gutter, ball is reflected back into play                
    #velocity of ball increased 10% everytime it strikes a paddle
    elif (ball_pos[0] >= (WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH)) and (ball_pos[1] >= paddle2_pos) and (ball_pos[1] <= paddle2_pos + PAD_HEIGHT):
        ball_vel[0] = -ball_vel[0] * 1.1
        
    #update ball's vertical position when ball collides and bounces off the top and bottom walls        
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
button1 = frame.add_button('Restart', new_game, 60)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# register event handlers

# start frame
new_game()
frame.start()
