friends = ["a", "b", "c", "d", "e", "f"]

print(friends[2], friends[3])

for x in friends:
    print(x)

colors = ["blue", "red","orange", "yellow", "green", "black", "grey"]
from turtle import *
circles = int(input("how many circles do you want?"))
tom = Turtle()
tom.speed(100)
from random import randrange
for c in range(circles):
    x = randrange(-350, 350)
    y = randrange(-350, 350)
    tom.penup()
    tom.goto(x, y)
    tom.pendown()
    tom.color(colors[c%7])
    tom.circle(30)
    print(c)
done()
