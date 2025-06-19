# Скрипт создания каталога товаров: сохранение каталога товаров в файл 'example.txt';
# можно дополнить каталог товаров, он сохранится в 'example.txt'.
catalog = {} # Создаём словарь - каталог товаров
with open('example.txt', 'r+') as f: # Открываем файл для чтения "r" и записи "+"
    # Цикл для чтения данных построчно с файла 'example.txt'и записи их в catalog
    for line in f:
        line = line.replace(':', ' ').split()
        catalog[line[0]] = int(line[1]) 
    for i in range(3): # Цикл для записей новых товоров в каталог
        product = input("Продукт: ")
        int_product = int(input("Сколько: "))
        if product in catalog: 
            catalog[product] += int_product
        else: catalog[product] = int_product
    f.seek(0) # Перенесение курсора к началу файла
    for s, t in catalog.items(): # Цикл для записи товаров из словаря в файл построчно
            f.write(f'{s} : {t}\n') # Стока где s ключ и t значение