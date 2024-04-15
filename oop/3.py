"""
Магический метод __new__
Разница между __init__ и __new__
__new__ - Вызывается перед созданием объекта класса
__init__ - Вызывается после создания объекта класса
"""


class Point:
    def __new__(cls, *args, **kwargs):
        print('Вызов функции __new__ для' + str(cls))
        return super().__new__(cls)
        # Возвращаем адрес нового объекта класса

    def __init__(self, x=0, y=0):
        print('Вызов функции __init__ ' + str(self))
        self.x = x
        self.y = y


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect_db(self):
        print(f'Соединение с сервером БД: {self.user} - {self.psw} - {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        print('Данные из БД')

    def write(self, data):
        print(f'Запись в БД: {data}')


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 80)

print(id(db), id(db2))
