from datetime import datetime
from assistant_bot.phrases import get_datetime, say_goodbye, greet, respond_to_call, say_mistake
from enum import Enum
from assistant_bot.daytime import get_part_of_day
from assistant_bot.settings import ASSISTANT_NAME, USER_NAME
from assistant_bot.intents import recognize_command, data

GREETING_WORDS = sorted(data["greeting"], key=len, reverse=True)


class AssistantStatus(Enum):
    ACTIVE = "active"
    WAITING = "waiting"
    EXIT = "exit"
    SLEEP = "sleep"


def handle_greeting() -> str:
    part_of_day = get_part_of_day(datetime.now())
    greeting_message = greet(part_of_day, USER_NAME)
    return greeting_message

def handle_exit() -> str:
    part_of_day = get_part_of_day(datetime.now())
    goodbye_message = say_goodbye(part_of_day, USER_NAME)
    return goodbye_message


def handle_time() -> str:
    time = get_datetime(datetime.now())
    time_message = (f"Сейчас {time['hours']} {time['minutes']}").strip()
    return time_message


def handle_mistake() -> str:
    mistake_message = say_mistake(USER_NAME)
    return mistake_message

def handle_call() ->str:
    call_message = respond_to_call(USER_NAME)
    return call_message

# команды
def handle(status: AssistantStatus, command_text: str) -> tuple[AssistantStatus, list[str]]:
    responses = []

    if ASSISTANT_NAME.lower() in command_text:
        command_text = command_text.replace(ASSISTANT_NAME.lower(), "").strip()


    for word in GREETING_WORDS:
        if word in command_text:
            command_text = command_text.replace(word, "").strip()
            responses.append(handle_greeting())
            break

    if not command_text:
        if not responses:
            responses.append(handle_call())
        status = AssistantStatus.WAITING
        return status, responses

    command_name, probability = recognize_command(command_text)

    if probability < 0.5:
        responses.append(handle_mistake())
        status = AssistantStatus.WAITING
    else:
        if command_name == "time":
            responses.append(handle_time())
            status = AssistantStatus.WAITING

        elif command_name == "greeting":
            responses.append(handle_greeting())
            status = AssistantStatus.WAITING

        elif command_name == "exit":
            responses.append(handle_exit())
            status = AssistantStatus.EXIT

        else:
            responses.append(handle_mistake())
            status = AssistantStatus.WAITING

    return status, responses

