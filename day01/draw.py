import turtle

t=turtle.Turtle()
t.speed(0)

def square(length, angle):
    for i in range(18):
        t.color("red")
        t.forward(length)
        t.right(angle)

def square1(length, angle):
    for i in range(18):
        t.color("blue")
        t.forward(length)
        t.right(angle)

def square2(length, angle):
    for i in range(18):
        t.color("green")
        t.forward(length)
        t.right(angle)                        

for i in range(11):
    square(50,20)
    t.right(11)
    square1(50,20)
    t.right(11)
    square2(50,20)
    t.right(11)