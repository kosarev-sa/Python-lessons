# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    def __str__(self):
        return "Попытка деления на ноль"


try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    if b == 0:
        raise MyZeroDivisionError
    c = a / b
except MyZeroDivisionError as error:
    print(error)
except ValueError:
    print("Неверное значение. Вводятся числа!")
else:
    print(f"Результат получен: = {c}")
