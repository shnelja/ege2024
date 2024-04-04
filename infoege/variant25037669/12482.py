from turtle import *
tracer(0)
screensize(8000, 8000)
left(90)
m = 30

down()
for i in range(4):
    fd(m*8)
    rt(90)
for i in range(4):
    lt(30)
    fd(6*m)
    rt(30)
    fd(8*m)
    rt(150)
    fd(6*m)
    lt(60)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(m * x, m * y)
        dot(5, 'red')
done()