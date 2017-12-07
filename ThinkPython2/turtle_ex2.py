import turtle

def square(t,length):
    
    t.pd()
    
    for i in range(4):
        t.fd(length)
        t.lt(90)

def bob():
    
    bob = turtle.Turtle()
    
    square(bob, 200)

    turtle.mainloop()

bob()
