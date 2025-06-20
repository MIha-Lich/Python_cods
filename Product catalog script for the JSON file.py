import json

catalog = {}
with open('test.json', 'r+') as f: 
    reading = json.loads(f.read())
    for line in reading: catalog[line] = int(reading[line])
    for i in range(3):
        product = input("Продукт: ")
        int_product = int(input("Сколько: "))
        if product in catalog: 
            catalog[str(product)] += int_product
        else: catalog[str(product)] = int_product
    f.seek(0)
    f.write(json.dumps(catalog))