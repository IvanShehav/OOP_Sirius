from turtle import *
screensize(2000, 2000)
tracer(0)
k = 30
left(90)

for i in range(2):
    forward(21*k)
    right(90)
    forward(27*k)
    right(90)
pu()
forward(9*k)
right(90)
forward(10*k)
left(90)
pd()
for i in range(2):
    forward(86*k)
    right(90)
    forward(47*k)
    right(90)
pu()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*k, y*k)
        dot(5,'red')

done()

print(13*18)