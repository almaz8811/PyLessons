# Пример 1
print('-' * 30, 'Пример 1')
class Point:
    # Атрибуты экземпляра
    def __init__(self, x, y):   # Конструктор
        self.x = x
        self.y = y
#    x = 0   # Атрибут класса
#    y = 0   # Атрибут класса
    # Метод экземпляра
    def coordinates(self):
        print(f'Координаты: x {self.x}, y {self.y}')

    def __repr__(self):
        return f'<Point x: {self.x}, y: {self.y}>'

#my_point = Point()  # my_point является объектом класса Point
my_point = Point(20, 5)  # my_point является объектом класса Point
my_point.coordinates()  # Вызываем метод coordinates()
print(my_point.x)

my_point.x = 10 # Изменим значение переменной x
my_point.coordinates()  # Вызываем метод coordinates()
print(my_point.x)
print(my_point)

# Пример 2
print('-' * 30, 'Пример 2')
class People:
#    man = 'мужчина' # Атрибут класса
#    girl = 'женщина'    # Атрибут класса
    def __init__(self, name):
        self.name = name
    # Метод экземпляра
    def sing(self, song):
        #return '{} играет на пианино - {}'.format(self.man.capitalize(), song)
        return '{} играет на пианино - {}'.format(self.name.capitalize(), song)

    def dance(self):
        #print('А {} танцует.'.format(self.girl))
        print('А {} танцует.'.format(self.name))

#object_1 = People() # Объект класса People
object_1 = People('Игорь') # Объект класса People
object_2 = People('Татьяна') # Объект класса People
#print(object_1.sing("'Лунную сонату'"))
print(object_1.sing("'Лунную сонату'"))
#object_1.dance()
object_2.dance()