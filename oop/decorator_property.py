"""
TODO Декоратор @property
Функция property() используется для определения свойств в классах.

Инкапсуляция в программировании — это принцип, согласно которому внутреннее устройство сущностей нужно
объединять в специальной «оболочке» и скрывать от вмешательств извне.
Доступ к объектам возможен через специальные открытые методы, а напрямую обратиться к их содержимому нельзя

Метод property() обеспечивает интерфейс для атрибутов экземпляра класса.
Он инкапсулирует атрибуты экземпляров и предоставляет свойства, аналогично тому, как это работает в Java и C#.

Метод property() принимает на вход методы get, set и delete, и возвращает объекты класса property.


"""


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    # old = property(get_old, set_old)

    @old.deleter
    def old(self):
        del self.__old





p = Person('Zayniddin', 20)
del p.old
print(p.__dict__)
p.get_old = 35
print(p.__dict__)