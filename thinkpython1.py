from swampy.TurtleWorld import *

world = TurtleWorld()
bob   = Turtle()
bob.delay = 0.01
def square(t,length):
  for i in range(4):
    fd(t,length)
    lt(t)

def polygon(t,length,n):
  for i in range(n):
    fd(t,length)
    lt(t,360.0/n)

def circle(t,r):
  polygon(t,2*r*3.1415926/40,40)

def arc(t,r,angle):
    length = 2*3.1415926*r/40
    for i in range(int(angle/360.0*40)):
        fd(t,length)
        lt(t,360.0/40)
#square(bob,50)
#polygon(bob,60,8)
#circle(bob,50)
arc(bob,angle = 360,r = 70)

wait_for_user()
