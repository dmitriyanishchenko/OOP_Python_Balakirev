class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y):  # вызываем инициализатор
        print("вызов инициализатора " + str(self))  # проверяем что запустился инициализатор
        self.x = x  # создаем локальные свойства x
        self.y = y  # создаем локальные свойства y

    def __del__(self):  # вызываем финализатор, который удалит экземпляр класса
        print("Удаление экземпляра  " + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point(1, 2)  # создаем экземпляр класса со значениями 1 и 2
print(pt.__dict__)  # выводим локальные свойства в консоль
