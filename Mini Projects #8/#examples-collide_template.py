# Testing template for collide method and group_collide function in RiceRcoks
# Only necessary code from Ricerocks template is included below

import math
import simplegui

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

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroids_blue.png, asteroids_brown.png, asteroids_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
    
# helper functin to determine distance between p and q    
def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
    
    
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
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)

    def update(self):
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

###################################################
# Student should add code for the collide method to Sprite class       
    
    # collide method
    
    # getter for radius
    
    # getter for position

####################################################
# Initialize sprites - rocks have radius 40, missiles have radius 3
rock0 = Sprite([0, 0], [0, 0], 0, 0, asteroid_image, asteroid_info)
rock1 = Sprite([40, 40], [0, 0], 0, 0, asteroid_image, asteroid_info)
rock2 = Sprite([0, 100], [0, 0], 0, 0, asteroid_image, asteroid_info)
missile0 = Sprite([0, 0], [0, 0], 0, 0, missile_image, missile_info)
missile1 = Sprite([0, 143], [0, 0], 0, 0, missile_image, missile_info)


####################################################
# Test code for collide method for Sprite class
# Note that method should always return True or False

print "Tests for collide method"
print rock0.collide(rock1)
print rock0.collide(rock2)
print rock1.collide(rock2)
print rock0.collide(missile0)
print rock1.collide(missile0)
print rock2.collide(missile1) # this test assume a collision if rock and missile touch


###################################################
# Output from collide tests

#Tests for collide method
#True
#False
#True
#True
#False
#True





####################################################
# Student should add code for the group_collide function here


####################################################
# Test code for group_collide function
# Note that function returns a number

#print 
#print "Tests for group_collide function"
#
#rock_group = set([rock0, rock1, rock2])
#print len(rock_group)
#print group_collide(rock_group, missile0)
#print len(rock_group)
#print rock0 in rock_group, rock1 in rock_group, rock2 in rock_group
#
#rock_group = set([rock0, rock1, rock2])
#print len(rock_group)
#print group_collide(rock_group, missile1)
#print len(rock_group)
#print rock0 in rock_group, rock1 in rock_group, rock2 in rock_group


###################################################
# Output from group_collide tests

#Tests for group_collide function
#3
#1
#2
#False True True
#3
#1
#2
#True True False
