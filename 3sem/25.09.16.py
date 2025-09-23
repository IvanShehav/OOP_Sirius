import math


class Shape:
    @property
    def area(self):
        raise NotImplementedError

    @property
    def perimeter(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = float(side)

    @property
    def area(self):
        return self.side ** 2

    @property
    def perimeter(self):
        return 4 * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        if ((a + b) < c) or ((b+c) < a) or ((a+c) < b):
            raise Exception("Треугольник не существует.")


    @property
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    @property
    def perimeter(self):
        return self.a + self.b + self.c


shapes = [Circle(5), Square(4), Rectangle(3, 6), Triangle(3, 4, 5)]

for shape in shapes:
    print(
        f"{shape.__class__.__name__}: площадь = {shape.area:.2f}, периметр = {shape.perimeter:.2f}"
    )


# print("Круг: площадь =", circle.area(), "периметр =", circle.perimetr())
# print("Квадрат: площадь =", square.area(), "периметр =", square.perimetr())
# print("Прямоугольник: площадь =", rectangle.area(), "периметр =", rectangle.perimetr())
# print("Треугольник: площадь =", triangle.area(), "периметр =", triangle.perimetr())



