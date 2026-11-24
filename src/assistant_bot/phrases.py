from datetime import datetime
from assistant_bot.daytime import PartOfDay
from num2words import num2words as n2w


HOURS = ("час", "часа", "часов")
MINUTES = ("минута", "минуты", "минут")
DEGREES = ("градус", "градуса", "градусов")


def greet(part: PartOfDay, user_name: str) -> str:
    if part == PartOfDay.MORNING:
        return f"Доброе утро, {user_name}!"
    elif part == PartOfDay.AFTERNOON:
        return f"Добрый день, {user_name}!"
    elif part == PartOfDay.EVENING:
        return f"Добрый вечер, {user_name}!"
    else:
        return f"Доброй ночи, {user_name}!"


def say_goodbye(part: PartOfDay, user_name: str) -> str:
    if part == PartOfDay.MORNING or part == PartOfDay.AFTERNOON:
        return f"Хорошего дня, {user_name}!"
    elif part == PartOfDay.EVENING:
        return f"Хорошего вечера, {user_name}!"
    else:
        return f"Спокойной ночи, {user_name}!"


def introduce(assistant_name: str) -> str:
    return f"Я {assistant_name}, персональный помощник."

# форма звучания слова в зависимости от числа
def get_plural_form(number: int, forms: tuple[str, str, str])-> str:
    one, few, many = forms
    last_digit = number % 10

    if 11<= number <= 14:
        return_str =  many
    elif last_digit == 1:
        return_str =  one
    elif 2 <= last_digit <= 4:
        return_str =  few
    else:
        return_str =  many
    return return_str

def get_datetime(now: datetime) ->dict:
    hours = now.hour
    time_hours_number_to_str = n2w(hours, lang='ru')
    time_hours_str = get_plural_form(hours, HOURS)
    hours_str = f"{time_hours_number_to_str} {time_hours_str}"

    minutes = now.minute
    time_minutes_number_to_str = n2w(minutes, lang='ru', gender="f")
    time_minutes_str = get_plural_form(minutes, MINUTES)
    minutes_str = f"{time_minutes_number_to_str} {time_minutes_str}"

    time = {"hours": hours_str, "minutes": minutes_str}
    return time

