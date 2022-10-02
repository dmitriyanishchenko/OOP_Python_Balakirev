class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y


v = Vector(1, 2)
res = Vector.get_coord(v)  # объявление классов обычным способом
print(res)

#                  ***   Cтатические методы  ***


class Vector:
    MIN_COORD = 0
    NAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.NAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):  #  проверка значений на валидаторе через classmethod
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod  #  - независимая сервисная функция, используется без self
    def norm2(x, y):
        return x * x + y * y


v = Vector(10, 20)
print(Vector.validate(15))  #  вызов метода класса непосредственно через сам класс
print(Vector.norm2(5, 6))
res = Vector.get_coord(v)  # объявление классов обычным способом
print(res)
