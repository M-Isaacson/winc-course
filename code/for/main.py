from typing import Counter
from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


""" Write your functions here. """

# Returns a list of country names that have the shortest length
def shortest_names(country_list):
    shortest_country_names = []
    previous_len           = 10
    for country in country_list:
        if len(country) > previous_len:
            continue
        elif len(country) == previous_len:
            shortest_country_names.append(country)
        else:
            shortest_country_names.clear()
            shortest_country_names.append(country)
            previous_len = len(country)
    return shortest_country_names

# Returns a list with the top three countries that have the most vowels in their name.
def most_vowels(country_list):
    countries_most_vowels = []
    country_checklist     = list(country_list)
    top_countries         = []
    previous_count        = 0
    vowel_count           = 0
    vowels                = list('aeiou')
    
    for x in range(3): # There are three positions to fill
        previous_count = 0 # Reset previous vowel counter.
        for country in country_checklist:
            # Get vowels from country name
            vowel_count = 0     # Reset the counted vowels
            for vowel in country:
                if vowel.casefold() in vowels:
                    vowel_count = vowel_count + 1
            if vowel_count < previous_count:
                continue
            elif vowel_count == previous_count:
                top_countries.append(country)
            else:
                top_countries.clear()
                top_countries.append(country)
                previous_count = vowel_count
        for top_country in top_countries:
            countries_most_vowels.append(top_country)
            country_checklist.remove(top_country)
        
        if len(countries_most_vowels) > 2:
            break
 
    return countries_most_vowels

# Returns a list of country names whose letters can be combined to form the complete alphabet
def alphabet_set(country_list):
    alphabet            = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_check      = alphabet
    alphabet_loop_check = alphabet
    previous_count      = 0 
    unique_count        = 0
    top_country         = ''
    alphabet_countries  = []
    loop_counter        = len(alphabet)

    while loop_counter > 0:
        previous_count = 0 # Reset previous unique character counter.

        # Find country with most unique characters in its name
        for country in country_list:    
            unique_count   = 0                   # Reset unique character counter.
            alphabet_check = alphabet_loop_check # When loop_counter decreases, charaters in alphabet_check decreases
            for char in country:                                     
                if char.casefold() in alphabet_check:                
                    unique_count   = unique_count + 1                
                    alphabet_check = alphabet_check.replace(char,'') 
            if unique_count > previous_count:
                previous_count  = unique_count
                top_country     = country
        
        # Set new values for while loop and add top_country to list
        for char in top_country:                                           
            if char.casefold() in alphabet_loop_check:                                         
                alphabet_loop_check = alphabet_loop_check.replace(char,'')

        alphabet_countries.append(top_country)
        
        loop_counter = len(alphabet_loop_check)

    return alphabet_countries       

    
# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()

    """ Write the calls to your functions here. """

    # List of countries that have the shortest length.
    print(shortest_names(countries))

    # List of countries that have the most vowels in their name.
    print(most_vowels(countries))

    # List of country names whose letters can be combined to form the complete alphabet.
    print(alphabet_set(countries))
