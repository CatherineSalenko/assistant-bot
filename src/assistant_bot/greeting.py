from assistant_bot.daytime import PartOfDay


def greet(part: PartOfDay, user_name: str) -> str:
    if part == PartOfDay.MORNING:
        return f"Доброе утро, {user_name}!"
    elif part == PartOfDay.AFTERNOON:
        return f"Добрый день, {user_name}!"
    elif part == PartOfDay.EVENING:
        return f"Добрый вечер, {user_name}!"
    else:
        return f"Доброй ночи, {user_name}!"


def introduce(assistant_name: str) -> str:
    return f"Я {assistant_name}, персональный помощник."
