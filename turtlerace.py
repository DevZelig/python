from turtle import *
from random import randrange

tom = Turtle()
jerry = Turtle()
tom.shape('square')
jerry.shape('circle')
tom.color('blue')
jerry.color('orange')

tom.penup()
jerry.penup()
tom.goto(-300, 150)
jerry.goto(-300, -150)

finishline = Turtle()
finishline.penup()
finishline.goto(300, 200)
finishline.pendown()
finishline.goto(300, -200)

ts = 0
js = 0
while ts < 600 and js < 600:
    t = randrange(2, 10)
    j = randrange(2, 10)
    tom.forward(t)
    jerry.forward(j)
    ts = ts + t
    js = js + j
    
done()