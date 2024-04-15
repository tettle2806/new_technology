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

    def __getattribute__(self, item):
        """
        TODO Управляет обращениями к атрибутам класса
        TODO Срабатывает автоматически
        :param item:
        :return:
        """
        if item == 'x':
            raise ValueError('Доступ запрещен')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """
        TODO Данный магический метод вызывается автоматически при создании экземпляра класса
        TODO С помощью него можно запретить создавать какой либо локальный атрибут в экземплярах класса
        TODO Пример
        :param key:
        :param value:
        :return:
        """
        if key =="z":
            raise AttributeError("Недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)
            # self.__dict__[key] = value так делать не стоит

    def __getattr__(self, item):
        """
        Вызывается автоматически каждый раз когда идет обращение к несуществующему атрибуту экземпляру класса
        :param item:
        :return:
        """
        return False


    def __delattr__(self, item):
        """
        Вызывается всякий раз когда удаляется определенный атрибут экземпляра класса
        :param item:
        :return:
        """
        print('__delattr__: ' + item)
        object.__delattr__(self, item) # Удаляет атрибуты

p1 = Point(1, 2)
p2 = Point(3 ,4 )
p1.y = 2
print(p1.MAX_COORD)
del p1.x
print(p1.__dict__)