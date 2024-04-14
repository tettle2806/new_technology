
class Point:
    color = 'red'
    circle = 2

    def set_coords(self):

        """
        :self - уникальный идентификатор экземпляра указывает на объект
        :return:
        """

        print(f'Вызов метода set_coords {self}')
        print(type(self))
        """
            Грубо говоря параметр self это ссылка которая указывает экземпляр класса то есть
            Без регистрации объекта функция set_coords не будет работать
            
            регистрация экземпляра класса pt = Point() и дальнейший вызов функции set_coords 
            без регистрации функция не будет работать Point.set_coords() выдаст ошибку
            
            TypeError: Point.set_coords() missing 1 required positional argument: 'self'
            
        """



