from datetime import datetime
from assistant_bot.daytime import get_part_of_day
from assistant_bot.phrases import greet, introduce
from assistant_bot.settings import USER_NAME, ASSISTANT_NAME
from assistant_bot.voice import speak


def main() -> None:
    now = datetime.now()
    part_of_day = get_part_of_day(now)
    greeting_message = greet(part_of_day, USER_NAME)
    print(greeting_message)
    introduction_message = introduce(ASSISTANT_NAME)
    print(introduction_message)
    speak([greeting_message, introduction_message])


if __name__ == "__main__":
    main()
