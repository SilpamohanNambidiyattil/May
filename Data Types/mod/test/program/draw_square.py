import turtle
s = turtle.Turtle()
n_side = 4
l_side = 70
s.fillcolor('blue')
s.begin_fill()
for i in range(n_side):
    s.forward(l_side)
    s.right(90)
s.end_fill()
turtle.done()