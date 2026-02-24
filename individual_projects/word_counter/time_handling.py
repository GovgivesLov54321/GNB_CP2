# GNB - 1st - Word Counter 3/3

from datetime import datetime
from zoneinfo import ZoneInfo


def get_current_timestamp():
    # America/Denver covers Utah (Mountain Time)
    utah_time = datetime.now(ZoneInfo("America/Denver"))
    formatted_time = utah_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time
