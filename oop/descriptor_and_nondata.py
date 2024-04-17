"""
TODO Дескрипторы

Вначале, что вообще такое дескрипторы? Это класс, который содержит или один магический метод __get__:

class A:
    def __get__(self, instance, owner):
        return ...

Или класс, в котором дополнительно прописаны методы __set__ и/или __del__:

class B:
    def __get__(self, instance, owner):
        return ...

    def __set__(self, instance, value):
        ...

    def __del__(self):
        ...
Первый (класс A) называется non-data descriptor (дескриптор не данных),
а второй (класс B) – data descriptor (дескриптор данных).
"""


class Integer:
    """
     Класс дескриптор
    """
    @classmethod
    def verify_coordinates(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата должна быть целым числом')

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coordinates(value)
        print(f"__set__: {self.name} = {value}")
        setattr(instance, self.name, value)



class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z



p = Point3D(1, 2, 3)
print(p.__dict__)
