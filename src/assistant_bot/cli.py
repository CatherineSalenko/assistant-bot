from datetime import datetime
from assistant_bot.voice import speak
from assistant_bot.commands import AssistantStatus, handle
from assistant_bot.listen import listen


def main() -> None:
    status = AssistantStatus.ACTIVE
    while status != AssistantStatus.EXIT:
        command = listen()
        print("Ты:", command)
        status, responses = handle(status, command)
        speak(responses)


if __name__ == "__main__":
    main()
