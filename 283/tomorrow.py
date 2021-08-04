import datetime


def tomorrow(today=datetime.date(2020, 7, 9)):
    return today + datetime.timedelta(days=1)
