"""
__bool__() - вызывается в приоритетном порядке функцией bool
__getitem__(self, item) – получение значения по ключу item;
__setitem__(self, key, value) – запись значения value по ключу key;
__delitem__(self, key) – удаление элемента по ключу key.
__iter__(self) – получение итератора для перебора объекта;
__next__(self) – переход к следующему значению и его считывание.

"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.y

    def __bool__(self):
        print("__bool__")
        return self.x ==self.y

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом")

        if 0 <= item < len(self.marks):
            return f"{self.marks[item]} + getitem"
        else:
            raise IndexError("Неверный индекс")


    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым не отрицательным")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")

        del self.marks[key]


s1 = Student('Sergey', [2,3,4,5])
print(s1.marks[0])
print(s1[2]) # getitem method
del s1[3]
s1[2] = 10
print(s1.marks)

class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.step = step
        self.stop = stop
        self.value = self.start - self.step
        # Здесь в инициализатор мы передаем начальное значение прогрессии, конечное и шаг изменения.
        # Также формируем свойство value, которое будет представлять собой текущее значение для считывания.

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

    def __iter__(self):
        self.value = self.start - self.step
        return self

fr = FRange(0.0, 5.0, 0.5)
it = iter(fr)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))