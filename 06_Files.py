with open('text.txt', 'w') as file:  # Открываем файл text.txt в переменную file. w - файл откроется для записи
    file.write('Напишем что-то!')

with open('text.txt', 'r') as file:
    for line in file:
        content = line.replace('\n', '')    # Убираем лишние переносы строк
        print(content)