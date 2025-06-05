import tkinter
import random
import time
# Создаю окно с помощью модуля tkinter
window = tkinter.Tk()
# Создаю холст 400 на 400
canvas = tkinter.Canvas(window, width=400, height=400)
canvas.pack()
# Список из 5 цветов
color = ["blue", "brown3", "burlywood1", "chartreuse", "cyan1"]  
# Пустой список для хранения словарей с данными о кругах
circles = []
# Цикл для создания словарей с параметрами каждого круга
for i in range(5):
    slov = {}
    # Задаю радиус кругу - случайное значение от 5 - 15
    r = random.randint(5, 15)
    # Задаю скорость передвижение круга в двух параметрах и записываю их в словарь
    slov['dx'] = random.randint(-10, 10)
    slov['dy'] = random.randint(-10, 10)
    # Задаю переменные со случайными значениями для создания точки появления круга
    x = random.randint(r, 400 - r)
    y = random.randint(r, 400 - r)
    # Создаю круг цвета соответствующего итерации и записываю его в словарь
    # с ключём 'id'
    slov['id'] = canvas.create_oval(x - r, y - r, x + r, y + r,  fill = color[i])
    # Помещаем в список словарь с параметрами круга
    circles.append(slov)
# Цикл задавающий направление движения кругов по холсту
while True:
    # Цикл помещает в переменную el словарь с данными круга из списка словарей
    for el in circles:
        # Проводится проверка, дошёл ли круг до края поля,
        # если да то меняется знак значения переменных dx и dy на отрицательный
        x0, y0, x1, y1 = canvas.coords(el['id'])
        el['dx'] *= -1 if x0 <= 0 or x1 >= 400  else 1
        el['dy'] *= -1 if y0 <= 0 or y1 >= 400  else 1
        # Метод для перемещения круга по холсту с указанной скоростью dx и dy
        canvas.move(el['id'], el['dx'], el['dy'])
    # Время между обновлениями кругов на холсте
    time.sleep(0.01)
    canvas.update()
window.mainloop()
