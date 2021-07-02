from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    return str(start_100days + timedelta(days=100))


get_hundred_days_end_date()


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    # return timedelta(pycon_date) - timedelta(pybites_founded)
    delta = pycon_date - pybites_founded
    return delta.days


get_days_between_pb_start_first_joint_pycon()
