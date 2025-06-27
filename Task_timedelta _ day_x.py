# Задача с timedelta: Написать программу, которая выводит информацию о том, сколько осталось времени до часа «Икс».
# Решение: 
import datetime
import sys
# Функция для добавления к цифре существительного в нужной форме
def number_words(number, word1, word2, word3):
    number_txt = f"{number} "
    if number % 100 in [11, 12, 13, 14]: number_txt += f"{word3}"
    elif number % 10 == 1: number_txt += f"{word1}"
    elif number % 10 in [2, 3, 4]: number_txt += f"{word2}"
    else: number_txt += f"{word3}"
    return number_txt

def timedelta_output_text(date_x, date_today):
    # Нахожу время timedelta - разницой между введёнными пользователем и актуалными временем и датой
    delta = (date_x - date_today)
    # Переменная с округлённым значением количества часов
    hours = delta.seconds // 3600
    # Переменная с округлённым значением количества минут
    minutes = delta.seconds % 3600 // 60
    text_day_X = 'До часа "Икс" '

    # Если кол-во дней болше 0, отображается их количество и существителное в нужной форме
    if delta.days > 0: text_day_X += number_words(delta.days, "день", "дня", "дней") + " "
    # Если дней осталось больше 1, добавится союз "и"
    if delta.days > 1 and (hours != 0 or minutes != 0): text_day_X += "и "
    # Если кол-во часов болше 0, отображается их количество и существителное в нужной форме
    if hours > 0: text_day_X += number_words(hours, "час", "часа", "часов") + " "
    # Если времени осталось больше часа, но меньше дня
    if hours > 1 and delta.days == 0 and minutes != 0: text_day_X += "и "
    # Если кол-во минут болше 0, отображается их количество и существителное в нужной форме
    if minutes > 0: text_day_X += number_words(minutes, "минута", "минуты", "минут")
    return print(text_day_X)
# С помощью модуля datetime в переменную вывожу текущее местное время и дату
# удаляю секунды и микросекунды, чтобы избежать ошибок в дальнейших расчётах
date_today = datetime.datetime.now().replace(second=0, microsecond=0)
date = input("Введите ДД.ММ.ГГГГ ЧЧ:ММ: ")
# Если пользователь вводит строку, несоответствующую формату, программа выведет на экран надпись «Ошибка».
try:
    # С помощью .datetime.strptime преобразовываем строку пользователя в объект datetime
    date_x = datetime.datetime.strptime(date, '%d.%m.%Y %H:%M')
except ValueError:
    print("Ошибка в вводе даты и времени.")
    sys.exit()
# Если время и дата введённое пользователем совпадает с текущим, будет показано запись в скобках
if date_x == date_today: print('Час "Икс" настал!')
elif date_x > date_today: timedelta_output_text(date_x, date_today)
# Если введенные дата/время меньше текущей
else: print("Ошибка. Дата указана раньше текущей")
