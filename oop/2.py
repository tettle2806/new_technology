"""
Инициализаторы и финализатор
"""

# __ имя магического метода __
# __init__ - инициализатор объекта
# __del__ - финализатор объекта

class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y):
        print('Вызов __init__')
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y



pt = Point(2,3)
print(pt.__dict__)
pt.set_coords(1, 2)
print(pt.__dict__)