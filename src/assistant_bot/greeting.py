from assistant_bot.daytime import PartOfDay


def greet(part: PartOfDay) -> str:
    if part == PartOfDay.MORNING:
        return "Доброе утро!"
    elif part == PartOfDay.AFTERNOON:
        return "Добрый день!"
    elif part == PartOfDay.EVENING:
        return "Добрый вечер!"
    else:
        return "Доброй ночи!"


