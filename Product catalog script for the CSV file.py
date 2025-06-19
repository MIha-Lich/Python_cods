# Скрипт создания каталога товаров: сохранение каталога товаров в файл 'test.csv'
import csv # Импортируем модуль csv

catalog = {} # Создаём словарь - каталог товаров
with open('test.csv', 'r+') as f: # Открываем файл для чтения "r" и записи "+"
    reading = csv.reader(f) # Создание объекта для чтения
    for line in reading: catalog[line[0]] = int(line[1])
    # Чтение файла 'test.csv' построчно, каждая строка список
    # Извлекая из списка объектов, помещаем в каталог как ключ и значение
    for i in range(3): # Цикл для записей новых товоров в каталог
        product = input("Продукт: ")
        int_product = int(input("Сколько: "))
        if product in catalog:
            catalog[product] += int_product
        else: catalog[product] = int_product
    f.seek(0) # Перенесение курсора к началу файла
    write = csv.writer(f) # Создание объекта для записи
    for s, t in catalog.items(): # Цикл для записи товаров из каталога в файл в виде списка
        write.writerow([s, t]) # Записи товаров из каталога в файл в виде списка построчно