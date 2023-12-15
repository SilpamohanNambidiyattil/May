import turtle
r = turtle.Turtle()
n_side = 4
l_side = 100
b_side = 40
r.fillcolor('blue')
r.begin_fill()
for i in range(n_side-2):
    r.forward(l_side)
    r.left(90)
    r.forward(b_side)
    r.left(90)
r.end_fill()
turtle.done()