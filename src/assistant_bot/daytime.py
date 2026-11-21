from datetime import datetime
from enum import Enum


class PartOfDay(Enum):
    MORNING = "morning"
    AFTERNOON = "afternoon"
    EVENING = "evening"
    NIGHT = "night"


def get_part_of_day(now: datetime) -> PartOfDay:
    if 5 <= now.hour < 12:
        return PartOfDay.MORNING
    elif 12 <= now.hour < 17:
        return PartOfDay.AFTERNOON
    elif 17 <= now.hour < 21:
        return PartOfDay.EVENING
    else:
        return PartOfDay.NIGHT
