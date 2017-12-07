import turtle

def polygon(t,length,n):
    
    t.pd()
    
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def bob():
    
    bob = turtle.Turtle()
    
    circle(bob,1)
    turtle.mainloop()

def circle(t, r):
         
    length = 2 * r
    n = 360 
    polygon(t, length, n)

bob()
