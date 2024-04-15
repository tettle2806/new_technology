"""
TODO Магические методы __setattr__, __delattr__, __getattribute__, __getattr__

TODO __setattr__(self,key, value) - автоматически вызывается при изменении свойства key класса;

TODO __getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item;

TODO __getattr__(self,item) - автоматически вызывается при получении несуществующего свойства item класса;

TODO __delattr__(self) - автоматически вызывается при удалении свойства item (не важно: существует оно или нет)

"""


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left
