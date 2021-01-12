import math
import turtle as t

t.penup()
t.goto(-720,0)
t.pendown()
for x in range(-720,720):
    t.goto(x,math.sin(math.radians(x))*100)
t.done()