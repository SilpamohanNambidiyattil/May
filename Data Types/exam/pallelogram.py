import turtle
t = turtle.Turtle()
side_h = 100
side_v = 50
t.fillcolor('green')
t.begin_fill()
for i in range(2):
    t.forward(side_h)
    t.left(60)
    t.forward(50)
    t.left(120)
t.end_fill()
turtle.done()