from datetime import datetime
from assistant_bot.daytime import get_part_of_day
from assistant_bot.greeting import greet
from assistant_bot.settings import USER_NAME


def main() -> None:
    now = datetime.now()
    part_of_day = get_part_of_day(now)
    greeting_message = greet(part_of_day, USER_NAME)
    print(greeting_message)

if __name__ == "__main__":
    main()
