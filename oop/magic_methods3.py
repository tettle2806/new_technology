"""
TODO Магические методы __str__(), __repl__(), __len__(), __abs__()

Метод isinstance() в Python используется для проверки принадлежности объекта к определенному классу или типу данных.

Каждый магический метод автоматически срабатывает в определенный момент времени, например:

__str__() – магический метод для отображения информации об объекте класса для пользователей
(например, для функций print, str);

__repr__() – магический метод для отображения информации об объекте класса в режиме отладки (для разработчиков).

__len__() – позволяет применять функцию len() к экземплярам класса;

__abs__() - позволяет применять функцию abs() к экземплярам класса.
Функция abs в Python возвращает абсолютное значение числа. Таким образом результат всегда положительный.
abs = модуль

__add__() – для операции сложения; x + y
__sub__() – для операции вычитания; x - y
__mul__() – для операции умножения; x * y
__truediv__() – для операции деления. x / y
__floordiv__() x // y
__mod__()  x % y

__iadd__   x += y
__isub__   x -= y
__imul__   x *= y
__itruediv__   x /= y
__ifloordiv__   x //= y
__imod__   x %= y

"""

class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return map(abs, self.__coords)


class Clock:
    __DAY = 86400 # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        #c1 = Clock(1000)
        #c2 = c1 + 1000
        #c4 = c3 + c2
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):
        # c3 = 1000 + c2
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Первый операнд должен быть типом int или объектом Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self


