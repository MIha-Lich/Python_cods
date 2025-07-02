# Программа для отображения кругов вокруг точки указанной курсором
import tkinter, random, time
# Создаю холст
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=300, height=200)
canvas.pack()
# Переменная где лежат 3 цвета
colors = ["brown2", "chartreuse3", "dark magenta"]
# Функция которая отчищает холст,
# затем рисует круг в нужной точке на холсте
def my_click(event):
    canvas.delete("all")
    radius_of_oval = random.randint(0,100)
    x = event.x; y = event.y; r = radius_of_oval
    circle = canvas.create_oval(x - r, y - r, x + r, y + r, outline = random.choice(colors))
    time.sleep(0.1)
    canvas.update()
# Метод который связывает функцию с
# событием нажатия левой кнопки мыши на холсте 
canvas.bind('<Button-1>', my_click)
# Команда запуска цикла обработки в графическом интерфейсе
window.mainloop()