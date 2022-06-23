import datetime
import calendar
from datetime import date


def getDates(start, end):
    def monthDate(day):
        suffix = ""
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
        return f'{day}{suffix}'

    values = []
    for i in range(1, 52):
        aDate = date.fromisocalendar(2022, i, 1)
        values.append(aDate.strftime(f'{monthDate(aDate.day)} %B %Y'))

    return values
