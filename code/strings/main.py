# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
"""
=================================
Assignment: Strings - Part 1
=================================
"""
# Players who scored.
dutch_scorer_1 = "Ruud Gullit"
dutch_scorer_2 = "Marco van Basten"

# The time a goal was made.
goal_0 = 32
goal_1 = 54

# Using the +-operator, create a string that reports on who scored when.
scorers = dutch_scorer_1 + " " + str(goal_0) + ", " + dutch_scorer_2 + " " + str(goal_1)

# Use f-strings or the +-operator to create a single string with information about who scored when. 
report = dutch_scorer_1 + " scored in the " + str(goal_0) + "nd minute\n" + dutch_scorer_2 + " scored in the " + str(goal_1) +"th minute"
#print(scorers)
#print(report)

"""
=================================
Assignment: Strings - Part 2
=================================
"""
# Name of a player.
player = "John van \'t Schip"
print(player)

# Firstname of the player.
first_name = player[:player.find(" ")]
print(first_name)

# Isolate and store the length of player"s last name.
last_name_len = len(player[player.find(" "):])-1
print(last_name_len)

# Isolate and store the player"s name (with abbreviated first name).
name_short = f"{player[0]}.{player[player.find(' '):]}"
print(name_short)

# The crowd chants the player"s name.
chant = (first_name + "! ") * len(first_name)
chant = chant[:len(chant)-1]
good_chant = player[-1] != " "
print(chant)
print(good_chant)
