# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Triangle:
    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c
        self.AB = self._katet(a, b)
        print('AB', self.AB)
        self.BC = self._katet(b, c)
        print('BC', self.BC)
        self.CA = self._katet(c, a)
        print('CA', self.CA)

    def _katet(self, a, b):
        AB = (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
        return AB ** 0.5

    def perimeter(self, ):
        return self.AB + self.BC + self.CA

    def height(self, ):
        p = 0.5 * (self.perimeter())
        h = (2 * (p * (p - self.AB) * (p - self.BC) * (p - self.CA)) ** 0.5) / self.AB
        return h

    def square(self):
        return (self.AB * self.height()) * 0.5


a = (-2, -5)
b = (-20, -20)
c = (-4, 0)
triangle = Triangle(a, b, c)
print('height', triangle.height())
print('perimeter', triangle.perimeter())
print('square', triangle.square())
