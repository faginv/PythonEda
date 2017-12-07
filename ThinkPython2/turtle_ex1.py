import turtle

def square(t):
    
    t.pd()
    
    for i in range(4):
        t.fd(100)
        t.lt(90)

def bob():
    
    bob = turtle.Turtle()
    
    square(bob)

    turtle.mainloop()

bob()
