import math
import turtle

def polyline(t, length, n, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t,length,n):
    
    angle = 360.0 / n

    polyline(t, length, n, angle)    
        
def bob():
    
    bob = turtle.Turtle()
    bob.pd()

    circle(bob,100)
    turtle.mainloop()

def circle(t, r):
         
    arc(t, r, 360)

def arc(t,r,angle):

    length = 2 * math.pi * r * angle / 360
    n = int(length / 3) + 1
    
    step_length = length / n
    step_angle = angle / n
    
    polyline(t, step_length, n, step_angle)

bob()
