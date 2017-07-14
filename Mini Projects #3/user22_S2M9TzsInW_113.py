# template for "Stopwatch: The Game"

#import modules
import simplegui

# define global variables
interval = 100
#time_count = 1490
time_count = 0
message = "0:00:0"
count_stop = 0
count_whole_seconds = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    #global time_count
    #time_test = 55
    #time_test += 1
    tens = t // 10
    seconds = tens % 60
    minutes = t // 600
    ones = t % 10
    if (seconds < 10):
        return str(minutes) + ":" + "0" + str(seconds) + "." + str(ones)
    else:
        return str(minutes) + ":" + str(seconds) + "." + str(ones)
    #return str(tens) + "." + str(ones)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    timer_count.start()

def stop_timer():
    global time_count, count_stop, count_whole_seconds
    if (timer_count.is_running()):
        timer_count.stop()
        count_stop += 1
        if ((time_count % 10) == 0):
            count_whole_seconds += 1

def reset_timer():
    global time_count, message, time_count, count_stop, count_whole_seconds
    if (timer_count.is_running):
        timer_count.stop()
    time_count = 0
    count_stop = 0
    count_whole_seconds = 0
    message = format(time_count)

# define event handler for timer with 0.1 sec interval
def tick():
    global interval, message, time_count
    time_count += 1
    #message = "time_count = " + str(time_count)
    message = format(time_count)
    #print format(time_count)

# define draw handler
def draw(canvas):
    #global message
    message2 = str(count_whole_seconds) + "/" + str(count_stop)
    canvas.draw_text(message,[50,112], 48, "Red")
    canvas.draw_text(message2,[160,15], 20, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200,200)

# register event handlers
frame.add_button("Start", start_timer, 200)
frame.add_button("Stop", stop_timer, 200)
frame.add_button("Reset", reset_timer, 200)
frame.set_draw_handler(draw)
timer_count = simplegui.create_timer(interval, tick)


# start frame
frame.start()
#timer_count.start()

# Please remember to review the grading rubric
