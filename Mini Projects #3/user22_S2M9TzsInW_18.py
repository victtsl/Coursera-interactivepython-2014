# template for "Stopwatch: The Game"

#import modules
import simplegui

# define global variables
interval = 100
timer_count = 0
message = "Hello"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    timer_count.start()

def stop_timer():
    timer_count.stop()

def reset_timer():
    pass

# define event handler for timer with 0.1 sec interval
def tick():
    global interval, message, timer_count
    message = "timer_count"
    frame.set_draw_handler(draw)
    print interval

# define draw handler
def draw(canvas):
    global message
    canvas.draw_text(message,[50,112], 48, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200,200)

# register event handlers
frame.add_button("Start", start_timer, 200)
frame.add_button("Stop", stop_timer, 200)
frame.add_button("Reset", reset_timer, 200)
timer_count = simplegui.create_timer(interval, tick)

# start frame
frame.start()
#timer_count.start()

# Please remember to review the grading rubric
