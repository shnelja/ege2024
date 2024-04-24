from turtle import *
tracer(0)
screensize(2000, 2000)
lt(90)
m = 30
down()

for i in range(3):
    down()
    for k in range(2):
        fd(7*m)
        rt(90)
        fd(7*m)
        rt(90)
    up()
    fd(6*m)
    rt(90)
    fd(6*m)
    lt(90)

up()
for x in range(-50, 51):
    for y in range(-50, 51):
        goto(x*m, y*m)
        dot(3, 'red')
exitonclick()
