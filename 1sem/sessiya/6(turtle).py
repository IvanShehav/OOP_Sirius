from turtle import *
tracer(0)
screensize(6000, 6000)
k = 30

left(90)
for i in range(2):
    forward(5*k)
    right(90)
    forward(11*k)
    right(90)
pu()
back(4*k)
right(90)
forward(6*k)
left(90)
pd()
for i in range(2):
    forward(42*k)
    right(90)
    forward(63*k)
    right(90)

pu()
for x in range(-70, 70):
    for y in range(-70,70):
        setpos(x*k, y*k)
        dot(5, 'red')
done()

print(43+62+62+43-4+16)