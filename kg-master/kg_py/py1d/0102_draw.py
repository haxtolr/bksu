
from turtle import *
t = Turtle()
t.speed(0)
i = 0

t.color("red")
while i < 1000:
   t.circle(10, i)
   t.fd(20)
   if i > 500:
       t.color("blue")
   i += 1
t.pu()
t.home()
t.pd()
i= 0
t.color("black")
while i < 1000:
    t.circle(10,-i)
    t.fd(20)
    if i > 500:
        t.color("yellow")
    i += 1
