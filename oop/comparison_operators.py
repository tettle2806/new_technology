"""
__eq__() – для равенства ==
__ne__() – для неравенства !=
__lt__() – для оператора меньше <
__le__() – для оператора меньше или равно <=
__gt__() – для оператора больше >
__ge__() – для оператора больше или равно >=
"""


class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен быть Clock или int")

        return other if isinstance(other, int) else  other.seconds

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc




c1 = Clock(1000)
c2 = Clock(2000)
print(c1 <= c2)