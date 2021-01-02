# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
    def __init__(self, A, B, C, D, name):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.AB = self._side(self.A, self.B)
        self.BC = self._side(self.B, self.C)
        self.CD = self._side(self.C, self.D)
        self.DA = self._side(self.D, self.A)
        self.test_name = name

    def _side(self, A, B):
        return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

    def get_all_side(self):
        print(f'AB {self.AB} BC {self.BC} CD {self.CD} DA {self.DA}')

    def is_trapezoid(self):
        base = self._parallel_horizontal()
        leg = self._parallel_vertikal()
        if base == leg:
            print('figure is parallelogram' if base else 'figure is quadrangle')
            return False
        print('figure is trapezoid')
        if base:
            if self.DA > self.BC:
                self.greater_base = self.DA
                self.lesser_base = self.BC
            else:
                self.greater_base = self.BC
                self.lesser_base = self.DA
            self.left_leg = self.AB
            self.right_leg = self.CD
            return True
        if self.CD > self.AB:
            self.greater_base = self.CD
            self.lesser_base = self.AB
        else:
            self.greater_base = self.AB
            self.lesser_base = self.CD
        self.left_leg = self.BC
        self.right_leg = self.DA
        return True

    def _parallel_horizontal(self, ):
        if self.B[1] - self.A[1] == self.C[1] - self.D[1] or self.A[1] - self.B[1] == self.D[1] - self.C[1]:
            return True
        return False

    def _parallel_vertikal(self, ):
        if self.C[0] - self.B[0] == self.D[0] - self.A[0] or self.B[0] - self.C[0] == self.A[0] - self.D[0]:
            return True
        return False

    def is_equilateral_trapezoid(self):
        if self.is_trapezoid():
            if self.left_leg == self.right_leg:
                print('is equilateral trapezoid')
                return True
            print('is not equilateral trapezoid')
            return False

    def perimeter(self):
        print(f'perimeter = {self.AB + self.BC + self.CD + self.DA}')

    def square(self):
        print(f'square = {((self.greater_base + self.lesser_base) / 2) * (self._height())}')

    def _height(self):
        return (self.left_leg ** 2 - ((self.greater_base - self.lesser_base) / 2) ** 2) ** 0.5


trapezoid_horizontal_good = Trapezoid((0, 0), (5, 10), (15, 10), (20, 0), 'horizontal_good')
trapezoid_vertical_good = Trapezoid((-1, -10), (-1, 10), (5, 5), (5, -5), 'vertical_good')
trapezoid_rectangular_bad = Trapezoid((0, 0), (10, 5), (15, 5), (15, 0), 'rectangular_bad')
trapezoid_parallelogram_bad = Trapezoid((0, 0), (5, 5), (25, 5), (20, 0), 'parallelogram_bad')
trapezoid_not_trapezoid_bad = Trapezoid((0, 0), (5, 6), (10, 15), (-1, 20), 'not_trapezoid_bad')

for trapezoid in [trapezoid_not_trapezoid_bad, trapezoid_parallelogram_bad, trapezoid_rectangular_bad,
                  trapezoid_vertical_good, trapezoid_horizontal_good]:
    print()
    print(f'===now {trapezoid.test_name}====')
    trapezoid.get_all_side()
    if trapezoid.is_equilateral_trapezoid():
        trapezoid.perimeter()
        trapezoid.square()
