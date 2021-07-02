import itertools
from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)
START_DATE = PYBITES_BORN + timedelta(days=100)


def gen_special_pybites_dates():
    from_date = START_DATE
    while True:
        yield from_date
        from_date = from_date + timedelta(days=100)


dates = itertools.islice(gen_special_pybites_dates(), 10)
list(dates)
