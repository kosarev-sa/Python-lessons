# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, dd_mm_yyyy):
        self.d = self.valid_date(*self.int_date(dd_mm_yyyy))[0]
        self.m = self.valid_date(*self.int_date(dd_mm_yyyy))[1]
        self.y = self.valid_date(*self.int_date(dd_mm_yyyy))[2]

    def __str__(self):
        return f'{self.d:02d}.{self.m:02d}.{self.y:04d}'

    @classmethod
    def int_date(cls, dd_mm_yyyy):
        for i in dd_mm_yyyy.split("-"):
            if not i.isdigit():
                raise TypeError("Введите дату в формате 'дд-мм-гггг'")
        return list(map(int, dd_mm_yyyy.split("-")))

    @staticmethod
    def valid_date(*args):
        d, m, y = args
        if d < 1 or d > 32:
            raise ValueError("День месяца должен быть в диапазоне от 1 до 31")
        elif m < 1 or m > 12:
            raise ValueError("Значение месяца должно быть в диапазоне от 1 до 12")
        elif y < 1 or y > 9999:
            raise ValueError("Значение года должно быть в диапазоне от 1 до 9999")
        else:
            return args


d1 = Date("01-04-2021")
print(d1)
print(d1.d, type(d1.d))
print(d1.m, type(d1.m))
print(d1.y, type(d1.y))

# d2 = Date("00-04-2021") #ValueError: День месяца должен быть в диапазоне от 1 до 31
# d3 = Date("01-13-2021") #ValueError: Значение месяца должно быть в диапазоне от 1 до 12
# d4 = Date("01-04-20212") #ValueError: Значение года должно быть в диапазоне от 1 до 9999
# d5 = Date("01-0m-2021") #TypeError: Введите дату в формате 'дд-мм-гггг'
