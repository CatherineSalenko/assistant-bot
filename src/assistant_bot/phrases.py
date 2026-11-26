from datetime import datetime
from assistant_bot.daytime import PartOfDay
from num2words import num2words as n2w
import json
import random

from assistant_bot.settings import ASSISTANT_NAME, USER_NAME


with open("data/responses.json", encoding="utf-8") as file:
    responses_file = json.load(file)

with open("data/plural.json", encoding="utf-8") as file:
    plural_file = json.load(file)


def get_message_greet(part: PartOfDay, user_name: str) -> str:
    default_phrases = responses_file["greeting"]["default"]

    if part == PartOfDay.MORNING:
        part_phrases = responses_file["greeting"]["morning"]
    elif part == PartOfDay.AFTERNOON:
        part_phrases = responses_file["greeting"]["afternoon"]
    elif part == PartOfDay.EVENING:
        part_phrases = responses_file["greeting"]["evening"]
    else:
        part_phrases = responses_file["greeting"]["night"]

    all_phrases = part_phrases + default_phrases
    greet_phras = random.choice(all_phrases)
    greet_message = greet_phras.format(user_name = user_name)

    return greet_message


def get_message_goodbye(part: PartOfDay, user_name: str) -> str:
    default_phrases = responses_file["goodbye"]["default"]

    if part == PartOfDay.MORNING or part == PartOfDay.AFTERNOON:
        part_phrases = responses_file["goodbye"]["afternoon"]
    elif part == PartOfDay.EVENING:
        part_phrases = responses_file["goodbye"]["evening"]
    else:
        part_phrases = responses_file["goodbye"]["night"]

    all_phrases = part_phrases + default_phrases
    goodbye_phras = random.choice(all_phrases)
    goodbye_message = goodbye_phras.format(user_name = user_name)
    return goodbye_message


def get_message_introduce(assistant_name: str) -> str:
    introduce_phras = random.choice(responses_file["introduce"])
    introduce_message = introduce_phras.format(assistant_name = ASSISTANT_NAME)
    return introduce_message


def get_message_call(user_name: str) ->str:
    call_phras = random.choice(responses_file["call"])
    call_message = call_phras.format(user_name = user_name)
    return call_message


def get_message_mistake(user_name:str) ->str:
    default_phrases = responses_file["mistakes"]["default"]
    #mistake_phras = random.choice(responses_file["mistakes"])
    all_phrases = default_phrases
    mistake_phrase = random.choice(all_phrases)
    mistake_message = mistake_phrase.format(user_name = user_name)
    return mistake_message

# форма звучания слова в зависимости от числа
def get_plural_form(number: int, forms: list[str])-> str:
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


def get_time_word(now: datetime) ->dict:
    hours = now.hour
    time_hours_number_to_str = n2w(hours, lang='ru')
    time_hours_str = get_plural_form(hours, plural_file["hours"])
    hours_str = f"{time_hours_number_to_str} {time_hours_str}"

    minutes = now.minute
    if minutes == 0:
        minutes_str = ""
    else:
        time_minutes_number_to_str = n2w(minutes, lang='ru', gender="f")
        time_minutes_str = get_plural_form(minutes, plural_file["minutes"])
        minutes_str = f"{time_minutes_number_to_str} {time_minutes_str}"

    time = {"hours": hours_str, "minutes": minutes_str}
    return time


def get_message_time(now: datetime)-> str:
    time_dict = get_time_word(now)
    hours = time_dict["hours"]
    minutes = time_dict["minutes"]

    time_phrases = random.choice(responses_file["time"])
    time_message = time_phrases.format(hours = hours, minutes = minutes).strip()
    return time_message

