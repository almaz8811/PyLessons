while True:
    try:
        a = 5
        b = int(input('Введите число: '))
        c = a / b
        print('Результат выполнения:', c)
        break
    except ValueError:
        print('Необходимо ввести целое число!')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')