#Скрипт создания каталога товаров и запись его в JSON-файл, сохранение и дополнение данных при новом запуске. 
#Ограничено 3 итерациями добавления товаров (можно изменить).
import json # Импортируем модуль json

with open('test.json', 'r+') as f: # Открываем файл для чтения "r" и записи "+"
    catalog = json.loads(f.read()) # Читаем файл test.json и десериализуем данные файла в формат python,
    # в переменную catalog - каталог товаров
    for i in range(3): # Цикл для записей новых товоров в каталог
        product = input("Продукт: ")
        int_product = int(input("Сколько: "))
        if product in catalog: # Если товар уже есть, то прибавляем количество уже к существующему товару
            catalog[str(product)] += int_product
        else: catalog[str(product)] = int_product
    f.seek(0) ) # Перенесение курсора к началу файла
    f.write(json.dumps(catalog)) # сериализуем данные файла в формат json и Записываем в файл test.json
