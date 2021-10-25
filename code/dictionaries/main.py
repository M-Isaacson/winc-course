from helpers import get_countries

__winc_id__ = "25a8041d2d5e4e3ab61ab1be43bfb863"
__human_name__ = "dictionaries"

"""
Exercise: Dictionaries
"""


def is_leap_year(year: int) -> bool:
    """
    Determines if a given year is a leap year.
    Source: https://www.wikihow.com/Calculate-Leap-Years.
    """
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
    """
    Checks if a given date is in ISO-8601 format.
    """
    if type(date) != str or len(date) != 10:
        return False
    delimiter_1 = date[4]
    delimiter_2 = date[7]
    the_year = date[:4]
    the_month = date[5:7]
    the_day = date[8:10]
    large_months = [1, 3, 5, 7, 8, 10, 12]
    small_months = [4, 6, 9, 11]
    # Are the delimiters correct?
    if delimiter_1 != "-" or delimiter_2 != "-":
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


def concat_msg(msg: str, add_msg: str) -> str:
    """
    Concatenates text in a message.
    """
    if msg != "":
        return msg + "\n" + add_msg
    else:
        return add_msg


def is_legit_nation(nation: str) -> bool:
    """
    Checks if nation is in list of countries.
    """
    countries = get_countries()
    if type(nation) != str:
        return False
    if nation in countries:
        return True
    else:
        return False


def create_passport(name: str, date_of_birth: str, place_of_birth: str, height: float, nationality: str) -> dict or str:
    """
    Creates a passport
    """
    passport_entry = {}
    error_msg = ""
    # Going thru parameters to check if it's ok to add to passport_entry.
    if type(name) == str:
        passport_entry["name"] = name
    else:
        error_msg = concat_msg(error_msg, "- Name has to be a string!")
    # Check if date of birth is in ISO-8601 format.
    if is_iso_8601(date_of_birth):
        passport_entry["date_of_birth"] = date_of_birth
    else:
        error_msg = concat_msg(error_msg, "- Date of birth has to be a string in ISO-8601 format!")
    if type(place_of_birth) == str:
        passport_entry["place_of_birth"] = place_of_birth
    else:
        error_msg = concat_msg(error_msg, "- Place of birth has to be a string!")
    if type(height) == float:
        passport_entry["height"] = height
    else:
        error_msg = concat_msg(error_msg, "- Height has to be in meters (e.g.: 1.72)")
    if is_legit_nation(nationality):
        passport_entry["nationality"] = nationality
    else:
        error_msg = concat_msg(error_msg, "- Nationality is not recognised")
    if error_msg == "":
        return passport_entry
    else:
        return error_msg


def add_stamp(passport: dict, country: str) -> dict:
    """
    Adds a stamp in a passport.
    """
    # If key 'stamps' doesn't exists then create one
    if passport.get("stamps") == None:
        passport["stamps"] = []
    if passport["nationality"] == country or country in passport["stamps"]:
        return passport
    else:
        passport["stamps"].append(country)

        return passport
    return passport


def check_passport(
    the_passport: dict, dest_country: str, allowed_to_travel_to: dict, forbidden_countries: dict
) -> bool:
    """
    Checks if  country to enter is allowed. If so create a stamp.
    """
    stamped_list = the_passport["stamps"]
    stamped_list.append(the_passport["nationality"])

    if dest_country not in allowed_to_travel_to[the_passport["nationality"]]:
        return False
    elif forbidden_countries.get(dest_country) != None:
        for stamp in stamped_list:
            if stamp in forbidden_countries[dest_country]:
                return False

    return add_stamp(the_passport, dest_country)


# This block is only executed if this script is run directly (python main.py).
# It is not run if you import this file as a module.
# if __name__ == "__main__":
#     passport = create_passport("Henk Jansen", "2021-03-03", "New York", 1.85, "Belgium")
#     allowed_to = {"Belgium": ["Netherlands", "Bulgaria"]}
#     forbidden = {"The Netherlands": ["Afghanistan"]}
