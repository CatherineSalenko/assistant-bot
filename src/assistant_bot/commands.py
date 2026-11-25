from datetime import datetime
from assistant_bot.phrases import get_datetime, say_goodbye, greet
from enum import Enum
from assistant_bot.daytime import get_part_of_day
from assistant_bot.settings import USER_NAME
from assistant_bot.intents import recognize_command


class AssistantStatus(Enum):
    ACTIVE = "active"
    WAITING = "waiting"
    EXIT = "exit"
    SLEEP = "sleep"


# команды
def handle(status: AssistantStatus, command: str) -> tuple[AssistantStatus, list[str]]:
    command_name, probability = recognize_command(command)
    if probability < 0.5:
        return AssistantStatus.WAITING, ["Извините, я не понимаю эту команду."]

    if command_name == "time":
        time = get_datetime(datetime.now())
        return AssistantStatus.WAITING, [f"Сейчас {time['hours']} {time['minutes']}"]

    elif command_name == "greeting":
        part_of_day = get_part_of_day(datetime.now())
        greeting_message = greet(part_of_day, USER_NAME)
        return AssistantStatus.WAITING, [greeting_message]

    elif command_name == "exit":
        part_of_day = get_part_of_day(datetime.now())
        goodbye_message = say_goodbye(part_of_day, USER_NAME)
        return AssistantStatus.EXIT, [goodbye_message]

    else:
        return AssistantStatus.WAITING, ["Извините, я не понимаю эту команду."]

