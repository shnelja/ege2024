from turtle import *
tracer(0)
lt(90)
m = 30
screensize(2000, 2000)

up()
backward(3*m)
rt(90)
backward(15*m)
lt(90)
down()
for i in range(2):
    fd(10*m)
    rt(90)
    fd(18*m)
    rt(90)
up()
backward(5*m)
rt(90)
fd(7*m)
lt(90)
down()
for i in range(2):
    fd(10*m)
    rt(90)
    fd(7*m)
    rt(90)
up()

for x in range(-20, 21):
    for y in range(-20, 21):
        goto(x*m, y*m)
        dot(8, 'red')

exitonclick()
