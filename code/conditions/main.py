# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

"""
======================
Exercise: Conditions
======================
"""

# Farm actions
def farm_action(weather,time_of_day,cow_need_milking,location_of_cows,season,is_slurry_tank_full,is_grass_long):

    if location_of_cows == 'pasture' and (weather=='rainy' or time_of_day == 'night'):
        return 'take cows to cowshed'
    elif cow_need_milking == True:
        if location_of_cows == 'pasture':
            return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
        else:
            return 'milk cows'
    elif is_slurry_tank_full == True and not (weather=='sunny' or weather=='windy'):
        if location_of_cows == 'pasture':
            return 'take cows to cowshed\nfertilize pasture\ntake cows back to pasture'
        else:
            return 'fertilize pasture' 
    elif is_grass_long == True and season == 'spring' and weather == 'sunny':
        if location_of_cows == 'pasture':
            return 'take cows to cowshed\nmow grass\ntake cows back to pasture'
        else:
            return 'mow grass'
    else:
        return 'wait'
