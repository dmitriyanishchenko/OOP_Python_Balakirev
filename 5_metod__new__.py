class Point:
    def __new__(cls, *args, **kwargs):  # метод вызывается в момент создания класса и наследуется от базового object
        print("вызов __new__ для " + str(cls))
        return super().__new__(cls)  # ссылается на ам класс

    def __init__(self, x=0, y=0):
        print("вызов __init__ для " + str(self))
        self.x = x
        self.y = y


pt = Point(1, 2)
print(pt)
