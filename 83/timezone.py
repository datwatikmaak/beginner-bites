from datetime import datetime
from pytz import timezone, utc

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')

naive_utc_dt = datetime(2018, 4, 27, 22, 55, 0)


def what_time_lives_pybites(naive_utc_dt: datetime):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    utc_dt = naive_utc_dt.replace(tzinfo=utc)
    dt_aus = AUSTRALIA.normalize(utc_dt.astimezone(AUSTRALIA))
    dt_es = SPAIN.normalize(utc_dt.astimezone(SPAIN))

    return dt_aus, dt_es
