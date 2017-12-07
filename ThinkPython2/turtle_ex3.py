import turtle

def polygon(t,length,n):
    
    t.pd()
    
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def bob():
    
    bob = turtle.Turtle()
    
    polygon(bob, 20, 114)
    turtle.mainloop()

bob()
