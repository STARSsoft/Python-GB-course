
from sys import argv

__all__ = ["is_valid_date"]


def is_valid_date(date_string: str) -> bool:
    """
    Функция, проверяющая, может ли дата существовать.

    """

    day, month, year = map(int, date_string.split('.'))
    if (year < 1 or year > 9999) or (month < 1 or month > 12):
        return False

    days_in_month = [
        31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < 1 or day > days_in_month[month-1]:
        return False
    return True


def is_leap_year(year: int) -> bool:
    """
    Функция, проверяющая, является ли год високосным.

    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


if __name__ == "__main__":

    if len(argv) == 2:
        _, d1 = argv
        print(f"{d1} {is_valid_date(d1)}")
    else:
        d1 = "12.10.2002"
        d2 = "45.10.1000"
        print(f"{d1} {is_valid_date(d1)}")
        print(f"{d2} {is_valid_date(d2)}")
