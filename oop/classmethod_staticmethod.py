"""
Декораторы classmethod и staticmethod
!!!!!
Прописывать имя класса внутри самого класса не верный ход лучше использовать self

!!!!!
Если функция будет использовать только атрибуты класса то используется classmethod

!!!!!
Если нужно написать независимую сервисную функцию которая будет использовать только параметры
переданные в нее то используем staticmethod
"""

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        """
        Декоратор работает только с атрибутами класса не с атрибутами объектов
        Полностью метод классов, не обращается к локальным атрибутам классов
        В нашем случае проверяет arg
        :param arg:
        :return:
        """
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self,x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        """
        staticmethod не получает доступа ни к объектам класса не данным внутри класса
        используется только данные переданные в функцию
        :param x:
        :param y:
        :return:
        """
        return x ** 2 + y ** 2

v = Vector(10, 20)
print(Vector.norm2(5, 6))
res = Vector.get_coord(v)
print(res)