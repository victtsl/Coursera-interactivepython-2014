# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5
angle_velocity = 0
is_thrusters = False
is_shoot = False
#a_rock = 0

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2013.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    global angle_velocity, is_thrusters
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "White", "White")          
        if is_thrusters:
            #draw image of ship with thrusters
            canvas.draw_image(self.image, [135,45], self.image_size, self.pos, self.image_size, self.angle)
        else:
            #draw image of ship with without thrusters
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        global move_forward
        friction = .8
        accel = 2
        move_forward = angle_to_vector(self.angle)
        self.vel = move_forward 
        if is_thrusters:
            self.vel[0] += move_forward[0] * accel
            self.vel[1] += move_forward[1] * accel
            #self.vel[0] += move_forward[0]
            #self.vel[1] += move_forward[1]
            
        self.vel[0] *= (1-friction)
        self.vel[1] *= (1-friction)
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.pos[0] %= 800
        self.pos[1] %= 600
        self.angle_vel = angle_velocity        
        self.angle += self.angle_vel
        #print "Self.Vel=", self.vel        
        #print "Self_pos=", self.pos   

    def shoot(self):
        global is_shoot, a_missile, move_forward
        cannon_pos_offset = 40
        cannon_vel_offset = 50
        cannon_pos = [0,0]
        cannon_vel = move_forward
        self_angle = angle_to_vector(self.angle)

        cannon_pos[0] = self.pos[0] + self_angle[0] * cannon_pos_offset
        cannon_pos[1] = self.pos[1] + self_angle[1] * cannon_pos_offset
        
        cannon_vel[0] += self.vel[0] * cannon_vel_offset
        cannon_vel[1] += self.vel[1] * cannon_vel_offset
        
        #print "Cannon_vel=", cannon_vel
        #print "Self_angle=", self.angle
        if is_shoot:
            #Create missile using def Sprite(pos, vel, ang, ang_vel, image, info, sound = None):
            #a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)
            a_missile = Sprite(cannon_pos, cannon_vel, 0, 0, missile_image, missile_info, missile_sound)
            #print "Shoot!"				
            #a_missile2 = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)
            

    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        
    def update(self):
        #self.angle = 50       
        #self.angle = random.randint(0,50)
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] +=  self.vel[1]
        self.pos[0] %= 800
        self.pos[1] %= 600
        
def draw(canvas):
    global time, is_shoot
    score = 10000
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    #draw lives remaining and the score
    canvas.draw_text("Lives:" , [550,50], 20, 'Red')
    canvas.draw_text(str(lives), [610,50], 20, 'Red')

    canvas.draw_text("Score:" , [640,50], 20, 'Green')
    canvas.draw_text(str(score), [700,50], 20, 'Green')
    
    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_rock1.draw(canvas)
    #a_missile.draw(canvas)
    
    if is_shoot:
        a_missile.draw(canvas)
        a_missile.update()    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_rock1.update()
    #a_missile.update()
            
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock, a_rock1
    random_ang_vel = 0.1
    random_int = random.randrange(-10,10)
    random_pos = [random.randint(0,800),random.randint(0,500)]
    random_vel = [random.randrange(-5,5),random.randrange(-5,5)]
    #random_ang_vel = (random.randrange(-10,10))/10
    if random_int != 0:
        random_ang_vel = random.random()/random_int
    #print "Random_Ang_vel=", random_ang_vel
    #a_rock1 = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
    a_rock1 = Sprite(random_pos, random_vel, 0, random_ang_vel, asteroid_image, asteroid_info)
    
# handler that make ship turn in response to left/right arrow keys
def ship_up(is_keydown):
    global is_thrusters
    if is_keydown:
        is_thrusters = True
        ship_thrust_sound.play()
    else:
        is_thrusters = False        
        ship_thrust_sound.rewind()
        
def ship_spacebar(is_keydown):
    global is_shoot
    if is_keydown:
        is_shoot = True
        #missile_sound.play()
        my_ship.shoot()
    else:
        is_missile = False    
        missile_sound.rewind() 
        
def ship_left(is_keydown):
    global angle_velocity
    if is_keydown:
        angle_velocity -= 0.2
    else:
        angle_velocity = 0

def ship_right(is_keydown):
    global angle_velocity
    if is_keydown:
        angle_velocity += 0.2
    else:
        angle_velocity = 0

inputs = {"up": ship_up,
          "left": ship_left,
          "right": ship_right,
          "space": ship_spacebar}

def keydown(key):
    is_keydown = True
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            inputs[i](is_keydown)

def keyup(key):
    is_keydown = False
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            inputs[i](is_keydown)

# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [1, 1], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
a_rock1 = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)

a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)
#a_missile2 = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
