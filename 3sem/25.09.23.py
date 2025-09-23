#в ткинтере визуализировать геометрические фигуры (точка, отрезки, треугольники, четырехугольники, окружность)
import tkinter
from Classes2309 import *
from tkinter import *
root = tkinter.Tk()
root.title("Рисунок")

canvas = tkinter.Canvas(root, width=1200, height=800, bg='white')
canvas.pack()

p1 = Point(100, 100)
p2 = Point(200, 150)

seg1 = Segment((p1.x, p1.y), (p2.x, p2.y))
seg2 = Segment((300, 300), (160, 500))

tri = Triangle([(200,200), (300, 200), (250, 300)])

sque = Polygone4([(300, 100), (400, 100), (400, 200), (300, 200)])


p1.draw(canvas)
p2.draw(canvas)
seg1.draw(canvas)
seg2.draw(canvas)
tri.draw(canvas)
sque.draw(canvas)


root.mainloop()

