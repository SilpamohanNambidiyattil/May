import turtle
p = turtle.Turtle()
n_side = 6
l_side = 70
angle = 360//n_side
p.fillcolor('red')
p.begin_fill()
for i in range(n_side):
    p.forward(l_side)
    p.right(angle)
p.end_fill()
turtle.done()