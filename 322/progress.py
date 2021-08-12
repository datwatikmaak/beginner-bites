from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    if not day_of_year:
        day_of_year = (datetime.today() - datetime(datetime.today().year, 1, 1)).days
    days_goal = books_goal / 365
    return (day_of_year * days_goal) <= books_read
