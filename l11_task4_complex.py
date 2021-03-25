# 4. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __str__(self):
        if self.b < 0:
            return f'{self.a}{self.b}i'
        elif self.b == 0:
            return f'{self.a}'
        else:
            return f'{self.a}+{self.b}i'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        a1 = self.a * other.a
        a2 = -(self.b * other.b)
        b1 = self.a * other.b
        b2 = self.b * other.a
        return Complex(a1+a2, b1+b2)


c1 = Complex(2, -2)
c2 = Complex(-3, 6)
c3 = c1 + c2
c4 = c1 * c2
print(f'c1 + c2 = {c1} + {c2} = {c3}')
print(f'c1 * c2 = ({c1}) * ({c2}) = {c4}')
