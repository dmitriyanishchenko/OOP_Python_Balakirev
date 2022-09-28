# class Point:  -  ключевое слово класс и имя класса с Большой буквы
#     pass  - заглушка

class Point:
    color = 'красный'  # атрибут класса
    circle = 2  # атрибут класса


col = Point.color  # обращаемся к атрибуту класса
cir = Point.circle
print(f'Цвет объекта - {col}, радиус объекта равен {cir} см.')
a = Point()  # создаем экземрляр класса
b = Point()  # создаем экземрляр класса

print(type(a)) #  выводим тип объекта в консоль
if type(a) == Point:
    print('Yes')
else:
    print('No')

print(isinstance(a, Point))  # проверяем, является ли объект а экземпляром класса Point
print(isinstance(b, Point))  # проверяем, является ли объект b экземпляром класса Point
print(a.__dict__)  # Проверяем пространство имен объекта а
print(b.__dict__)  # Проверяем пространство имен объекта b
print(a.color)  # выводим в консоль значение атрибута color
print(a.circle)  # выводим в консоль значение атрибута circle
a.color = 'green'  # переобредялем в объекте а значение атрибута color
print(a.color)  #  проверяем, что значение атрибута color в экземпляре класса а  изменилось
print(b.color)  # проверяем, что значение атрибута color в экземпляре класса b не изменилось
print(a.__dict__)   # проверяем пространство имен экземпляра а
Point.type_pt = 'disk'  # в класс добавляем атрибут type_pt и присваиваем ему значение 'disk'
setattr(Point, 'prop', 1)  # команда для динамического добавления атрибута в класс и его значения
print(Point.__dict__)
setattr(Point, 'type_pt', 2)  # команда для замены значения атрибута, если он уже существует
print(Point.type_pt)
# getattr(Point, 'a')  # возвращает  ошибку,  если нет такого аттрибута
print(getattr(Point, 'a', False))  # возвращает  False,  если нет такого аттрибута

del Point.type_pt  # Удаление атрибута type_pt из класса Point
print(Point.__dict__)

















