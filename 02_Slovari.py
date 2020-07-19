'''
Тип данных - Списки
'''
# Создаем список имен
# У каждого элемена свой номер, нумерация начинается с 0
name = ['Иван', 'Дмитрий', 'Петр', 'Павел']
# Выведим список на экран
print(name)
# Посчитаем количество элементов в списке
print(len(name))
# Добавим еще один элемент в список name
name.append('Марина')
print(name)
# Подсчет количества, сколько раз в списке встречается данный элемент
print(name.count('Иван'))
print(name.count('Валерия'))
# Получение превого элемента с нулевым индексом
print(name[0])
# Получение последнего элемента
print(name[-1])
# Получение части списка при помощи среза
print(name[0:3])
# Получение индекса элемента
print(name.index('Павел'))
# Сортировка элементов списка
name.sort()
print(name)
# Работа оператора in
print('Валерия' in name)
print('Марина' in name)
# Удаление элемента по индексу
print(name)
del name[0]
print(name)
# Удаление элемента по названию
name.remove('Иван')
print(name)

'''
Тип данных - Словари
'''
# В переменной phone_book создаем словарь с элементами ключ:значение
phone_book = {
    'name': 'Иван',
    'city': 'Москва',
    'phone': '999-99-99'}
# Выведим на экран значения phone_book
print(phone_book)
# Выведим количество элементов словаря
print(len(phone_book))
# Обновим значение элемента city
phone_book['city'] = 'Екатеринбург'
print(phone_book)
# Добавляем новый элемент year_birth со значением 1980
phone_book['year_birth'] = 1980
print(phone_book)
# Получаем значение ключа name
print(phone_book['name'])
# Проверяем наличие ключа name и age
print(phone_book.get('age'))
print(phone_book.get('name'))
# Удаляем из сковаря элемент year_birth и его значение
del phone_book['year_birth']
print(phone_book)

'''
Список помещаем в словарь
'''
