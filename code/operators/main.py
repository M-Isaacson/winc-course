# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

"""
====================================================
A comparison between Spain and Switzerland 
based on the CIA World Factbook's one page summaries
====================================================
"""

# The language spoken the most in Switzerland is the same as in Spain.
switzerland_language  = 'German'
spain_language        = 'Castilian Spanish'
print(switzerland_language == spain_language)

# The most prevalent religion in Switzerland is the same as in Spain.
switzerland_religion  = 'Roman Catholic'
spain_religion        = 'Roman Catholic'
print(switzerland_religion == spain_religion)

# The name length of Spain's capital does not equal that of Switzerland.
spain_capital_name_length       = len('Madrid')
switzerland_capital_name_length = len('Bern')
print(spain_capital_name_length != switzerland_capital_name_length)

# Switzerland's GDP is greater than Spain's GDP.
switzerland_gdp = 580000000000
spain_gdp       = 1778000000000
print(switzerland_gdp > spain_gdp)

# The population growth is less than 1% in Switzerland and Spain.
switzerland_population_growth = 0.66
spain_population_growth       = 0.67
percent_control_value         = 1

print((switzerland_population_growth < percent_control_value) and (spain_population_growth < percent_control_value))

# At least one of the two countries has a population count of over 10 million.
switzerland_total_population  = 50000000
spain_total_population        = 8400000
population_control_value      = 10000000

print((switzerland_total_population > population_control_value) or (spain_total_population > population_control_value))

# Exactly one of the two countries has a population count of over 10 million.
print((switzerland_total_population > population_control_value) or (spain_total_population > population_control_value))