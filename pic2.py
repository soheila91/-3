import turtle
t= turtle.Turtle()
t.speed(-1)
length=10
step=10

for i in range(20):
    t.fd(length)
    t.left(45)
    length +=step
    
