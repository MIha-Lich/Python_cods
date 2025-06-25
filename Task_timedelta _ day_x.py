# Задача с timedelta: Написать программу, которая выводит информацию о том, сколько осталось времени до часа «Икс».
# Решение:
import datetime

def choose_plural(s, k):
    if s % 100 in [11,12,13,14]: return f"{s} {k[2]}"
    if s % 10 == 1: return f"{s} {k[0]}"
    if s % 10 in [2, 3, 4]: return f"{s} {k[1]}"
    return f"{s} {k[2]}"

try:
    date_today = datetime.datetime.now().replace(second=0, microsecond=0)
    date = input("Введите ДД.ММ.ГГГГ ЧЧ:ММ: ")
    date_x = datetime.datetime.strptime(date, '%d.%m.%Y %H:%M')
    if date_x > date_today:
        delta = (date_x - date_today)
        h = delta.seconds // 3600
        
        if not delta.days == 0: day = choose_plural(delta.days, ("день", "дня", "дней"))
        else: day = ""
        hour = choose_plural(h, ("час", "часа", "часов"))
        if not h == 0: hours = hour
        else: hours = "" 
        minute = choose_plural((delta.seconds % 3600 // 60), ("минута", "минуты", "минут"))
        if not (delta.seconds % 3600 // 60) == 0: minutes = minute
        else: minutes = ""
        
        if delta.days > 1: print(f'До часа "Икс" {day} и {hour} {minute}')
        elif h > 1 and day == "": print(f'До часа "Икс" {hour} и {minute}')
        elif "" in [day, hours, minutes]: print(f'Час "Икс" сегодня')
        else: print(f'До часа "Икс" {day} {hours} {minutes}')
    else: print("Ошибка")
except ValueError:
    print("Ошибка")