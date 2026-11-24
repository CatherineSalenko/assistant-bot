from datetime import datetime
from assistant_bot.phrases import get_datetime


def handle(command: str) -> list[str]:
    if "время" in command or "времени" in command or "час" in command :
        time = get_datetime(datetime.now())
        return [f"Сейчас {time['hours']} {time['minutes']}"]
    else:
        return ["Извините, я не понимаю эту команду."]

