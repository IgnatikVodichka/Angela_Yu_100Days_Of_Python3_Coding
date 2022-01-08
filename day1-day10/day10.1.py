

def is_leap(year):
    '''This is a doc string'''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(what_year, month):
    """ And this is a doc string"""
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if what_year and month == 2:
        return 29
    return month_days[month - 1]


year = int(input("Please enter Year: "))
month = int(input("Please enter Month: "))

what_year = is_leap(year)
what_month = days_in_month(what_year, month)

print(what_month)
