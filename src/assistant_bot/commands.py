from datetime import datetime
from assistant_bot.phrases import get_datetime, say_goodbye, greet
from enum import Enum
from assistant_bot.daytime import get_part_of_day
from assistant_bot.settings import USER_NAME


TIME_WORDS = ("время", "времени", "час")
EXIT_WORDS = ("на сегодня хватит", "спокойной ночи", "на сегодня закончили", "выключись", "на сегодня все")
GREETING_WORDS = ("привет", "здравствуй", "добрый день", "доброе утро", "добрый вечер","доброй ночи", "приветики")

class AssistantStatus(Enum):
    ACTIVE = "active"
    WAITING = "waiting"
    EXIT = "exit"
    SLEEP = "sleep"


def has_any_word(command: str, words: tuple[str,...]) -> bool:
    for word in words:
        if word in command:
            return True
    return False

# команды
def handle(status: AssistantStatus, command: str) -> tuple[AssistantStatus, list[str]]:
    if has_any_word(command, TIME_WORDS):
        time = get_datetime(datetime.now())
        return AssistantStatus.WAITING, [f"Сейчас {time['hours']} {time['minutes']}"]

    elif has_any_word(command, GREETING_WORDS):
        part_of_day = get_part_of_day(datetime.now())
        greeting_message = greet(part_of_day, USER_NAME)
        return AssistantStatus.WAITING, [greeting_message]

    elif has_any_word(command, EXIT_WORDS):
        part_of_day = get_part_of_day(datetime.now())
        goodbye_message = say_goodbye(part_of_day, USER_NAME)
        return AssistantStatus.EXIT, [goodbye_message]

    else:
        return AssistantStatus.WAITING, ["Извините, я не понимаю эту команду."]

