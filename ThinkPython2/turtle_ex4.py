import math
import turtle

def polygon(t,length,n):
    
    t.pd()
    
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def bob():
    
    bob = turtle.Turtle()
    
    circle(bob, 1)
    turtle.mainloop()

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
 
    polygon(t, length, n)

bob()
