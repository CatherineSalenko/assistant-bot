from datetime import datetime
from assistant_bot.daytime import get_part_of_day
from assistant_bot.greeting import greet


def main() -> None:
    now = datetime.now()
    part_of_day = get_part_of_day(now)
    greeting_message = greet(part_of_day)
    print(greeting_message)

