from turtle import *
tracer(0)
m = 50
screensize(3000,3000)
left(90)

for i in range(4):
    for j in range(4):
        forward(8*m)
        right(90)
    forward(13*m)
    right(90)
    forward(4*m)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*m,y*m)
        dot(5, 'red')

done()