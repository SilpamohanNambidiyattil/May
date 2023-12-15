""" program to draw a circle and fill the circle with a color """

import turtle
t = turtle.Turtle()
r = 100
t.fillcolor('red')
t.begin_fill()
t.circle(r)
t.end_fill()
turtle.done()


def drawCircle(self):
    t = turtle.Turtle()
    t.fillcolor(self.color)
    t.begin_fill()
    t.circle(self.radius)
    t.end_fill()
    turtle.done()