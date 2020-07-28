"""Импортируем модуль datetime для работы с датой и временем,
    добавляем timedelta для работы с разницей"""
from datetime import datetime, timedelta
import locale

# Работа с datetime
time_now = datetime.now()   # Текущее системное время и дата на компьютере
print(time_now) # Выводим на экран переменную time_now

time_create = datetime(2019, 1, 1)  # Создаем произвольное время и дату
print(time_create)

delta = time_now - time_create  # Разница между датами
print(delta, '\n')

# Работа с timedelta
days = timedelta(days = 1)  # Создали timedelta, в которой лежит один день
delta = time_create - days  # Производим математические действия
print(delta.strftime('%d.%m.%Y'))   # Выводим на экран значение delta изменив формат даты
print(delta.strftime('%A %d %B %Y'))    # Еще один формат даты

# Работа с locale
locale.setlocale(locale.LC_TIME, 'ru_RU')   # Переводим на русский язык
print(delta.strftime('%A %d %B %Y').capitalize()) # Понедельник с большой буквы

# Получение даты из строки
locale.setlocale(locale.LC_TIME, 'ru_RU')   # Переводим на русский язык
birthday = input('\nВведите ваши данные в формате день.месяц.год: ')
weekday = datetime.strptime(birthday, '%d.%m.%Y').strftime('%A').upper()    # %A - берем только день недели
                                                                            # upper() - текст заглавными буквами"""
print(f'\nВ {weekday} вас мама родила!')

# Возможные форматы вывода даты на экран
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes