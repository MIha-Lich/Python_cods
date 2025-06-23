import datetime # Импортирую модуль datetime
import tkinter # Импортирую модуль tkinter

# Создаю окно-холст для отображения циферблата
window = tkinter.Tk() 
canvas = tkinter.Canvas(window)
canvas.pack()

# Переменная для отображения текста на холсте (точка где начинается текст) в конкретном формате, размере, и цвете
test = canvas.create_text(150, 100, font=('Arial', 30), fill="Red")

# Вечный цикл который выводит и обнавляет время на холсте
while True:
    my_datetime = datetime.datetime.now() # Выводит время целиком
    my_datetime1 = my_datetime.strftime("%H:%M:%S") # выводит Час:Минута:Секунда
    # Вводит изменение в переменную test заменяя/вводя значение опцию ввоода текста
    canvas.itemconfig(test, text=my_datetime1)
    canvas.update() # Обновление отображения содержимого холста