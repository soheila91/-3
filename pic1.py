import turtle
t= turtle.Turtle()
t.speed(0)
length=10
step=10

for i in range(20):
    t.fd(length)
    t.left(90)
    length +=step
    
