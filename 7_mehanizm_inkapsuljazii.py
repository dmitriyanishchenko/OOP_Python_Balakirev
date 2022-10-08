from accessify import private, protected


class Point:
    def __init__(self, x=0, y=0):
        self.x = x  # свойства 'public'
        self.y = y


pt = Point(1, 2)
pt.x = 200
pt.y = 'coord_y'  # недопустимое присвоене строкового литерала значению координаты y
print(pt.x, pt.y)


#           ***    Механизм инкапсуляции   ***
#  attribute (без одного или двух подчеркиваний вначале)  - публичное свойство (public)
#  _attribute (с одним подчеркиванием) - режим доступа protected (сдужит для обращения внутри класса
#       и во всех дочерних классах.
#  __attribute (с двумя подчеркиваниями) - режим доступа private, служит для обращения только внутри класса

# режим доступа 'protected'


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


pt = Point(1, 2)
print(pt._x, pt._y)  # когда режим protected, то можно изменить через ссылку pt изменить свойства через экземпляр класса


# режим доступа  'private'
class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x  # свойства 'protected'
            self.__y = y

    # @private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):  # вспомогательный метод - СЕТТЕР
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами!!!")

    def get_coord(self):  # вспомогательный метод - геттер,  который работают с защищенными локальными атрибутами
        return self.__x, self.__y


pt = Point(1, 2)
print(pt.get_coord())
