from helpers import get_countries

__winc_id__ = '25a8041d2d5e4e3ab61ab1be43bfb863'
__human_name__ = 'dictionaries'


"""
========================
Exercise: Dictionaries
========================
"""


def is_leap_year(year: int) -> bool:
    if type(year) != int:
        return False
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

def is_iso_8601(date: str) -> bool:
    # First check if parameter is string and length is correct.
    if type(date) != str or len(date) != 10:
        return False
    # Set variables
    delimiter_1 = date[4]
    delimiter_2 = date[7]
    the_year = date[:4]
    the_month = date[5:7]
    the_day = date[8:10]
    large_months = [1, 3, 5, 7, 8, 10, 12]
    small_months = [4, 6, 9, 11]
    # Are the delimiters correct?
    if delimiter_1 != '-' or delimiter_2 != '-':
        return False
    # Check if year, month and day are numeric.
    if (the_year.isnumeric() is False) or (the_month.isnumeric() is False) or (the_day.isnumeric() is False):
        return False
    # Check if month has a number between '0' and '13'.
    if (int(the_month) < 1) or (int(the_month) > 13):
        return False
    # Is the day number appropriate for the related month.
    if (int(the_month) in large_months) and ((int(the_day) < 0) or (int(the_day) > 32)):
        return False
    if (int(the_month) in small_months) and ((int(the_day) < 0) or (int(the_day) > 31)):
        return False
    if int(the_month) == 2:
        if (is_leap_year(int(the_year)) == True) and ((int(the_day) < 0) or (int(the_day) > 30)):
            return False
        if (is_leap_year(int(the_year)) == False) and ((int(the_day) < 0) or (int(the_day) > 29)):
            return False    
    return True


def create_passport(
    name: str,
    date_of_birth: str,
    place_of_birth: str,
    height: float,
    nationality: str
) -> dict:
    passport_entry = {}
    # Going thru parameters to check if it's ok to add to passport_entry.
    if type(name) == str:
        passport_entry['name'] = name
    else:
        return 'Name has to be a string!'
    # if type(date_of_birth) == str:
        # Check if string is in ISO 8601 format.
    return passport_entry


# This block is only executed if this script is run directly (python main.py).
# It is not run if you import this file as a module.
if __name__ == '__main__':
    # Create_passport('Henk Jansen', '2021-03-03', 'New York', 1.87, 'German')
    print(is_iso_8601('2022-12-20'))
