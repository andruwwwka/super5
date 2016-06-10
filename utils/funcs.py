import datetime
import calendar


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def add_months(sourcedate, months):
    if sourcedate.month < 12:
        month = sourcedate.month - 1 + months
        year = int(sourcedate.year + month / 12)
        month = month % 12 + 1
    else:
        month = 1
        year = sourcedate.year + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def sub_months(sourcedate, months):
    if 1 < sourcedate.month < 12:
        month = sourcedate.month - 1 + months
        year = int(sourcedate.year + month / 12)
        month = month % 12 - 1
    elif sourcedate.month == 12:
        year = sourcedate.year
        month = 11
    else:
        month = 12
        year = sourcedate.year - 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def month_text(month):
    MONTHS = [
        'Январь',
        'Февраль',
        'Март',
        'Апрель',
        'Май',
        'Июнь',
        'Июль',
        'Август',
        'Сентябрь',
        'Октябрь',
        'Ноябрь',
        'Декабрь',
    ]
    return MONTHS[month - 1]
