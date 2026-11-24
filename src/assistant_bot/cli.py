from datetime import datetime
from assistant_bot.daytime import get_part_of_day
from assistant_bot.phrases import greet, introduce
from assistant_bot.settings import USER_NAME, ASSISTANT_NAME
from assistant_bot.voice import speak
from assistant_bot.commands import AssistantStatus, handle
from assistant_bot.listen import listen


def main() -> None:
    # now = datetime.now()
    # part_of_day = get_part_of_day(now)
    # greeting_message = greet(part_of_day, USER_NAME)
    # print(greeting_message)
    # introduction_message = introduce(ASSISTANT_NAME)
    # print(introduction_message)
    # speak([greeting_message, introduction_message])

    status = AssistantStatus.ACTIVE
    while status != AssistantStatus.EXIT:
        command = listen()
        print("Ты:", command)
        status, responses = handle(status, command)
        speak(responses)


if __name__ == "__main__":
    main()
