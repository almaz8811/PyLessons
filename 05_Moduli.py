from collections import Counter

parking = ['Audi', 'BMW', 'Audi', 'Lada', "Audi"]
brand = Counter(parking)
print('\nПосчитаем повторяющиеся элементы из списка parking:', brand)

print('\nНапечатаем каждый элемент словаря на новой строчке:')
for total in brand:
    print(total, '\t', brand[total])

text = Counter(parking[3])
print('\nПосчитаем повторяющиеся буква в слове LADA:', text)