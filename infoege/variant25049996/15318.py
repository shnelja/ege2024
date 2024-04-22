from turtle import *
tracer(0)
screensize(2000, 2000)
lt(90)
m = 30
down()

for i in range(2):
    fd(13*m)
    rt(90)
    fd(18*m)
    rt(90)
up()
fd(5*m)
rt(90)
fd(9*m)
lt(90)
down()
for i in range(2):
    fd(11 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(4, 'red')
exitonclick()
