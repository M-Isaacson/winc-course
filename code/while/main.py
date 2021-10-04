from helpers import random_koala_fact

__winc_id__ = 'c0dc6e00dfac46aab88296601c32669f'
__human_name__ = 'while'

"""
==========
Functions
==========
"""
def unique_koala_facts(unique_items: int) -> list:
    random_fact = ''
    count       = 0
    unique_set  = set()
    unique_list = list()
    while count < 1000:
        # Get random fact
        random_fact = random_koala_fact()
        # Check if fact is already in list
        unique_set.add(random_fact)
        # If limmit is reached, break out of loop
        if len(unique_set) == unique_items:break
        # Upping the count
        count += 1
    # Add all unique items in a list
    for koala_fact in unique_set:unique_list.append(koala_fact)

    return unique_list

def num_joey_facts() -> int:
    random_fact    = ''
    repeated_facts = {}
    count = 0
    while count < 10:
        # Get random fact
        random_fact = random_koala_fact()
        # Does string containing 'joey'
        if random_fact.casefold().find('joey') > 0:
            # Search dictionary
            if random_fact in repeated_facts:
                # Upping the value if in dictionary
                repeated_facts.update({random_fact:repeated_facts[random_fact] + 1})
                count = repeated_facts[random_fact]
            else:
                # Add new key-value pair to dictionary
                repeated_facts[random_fact] = 1

    return len(repeated_facts)

def koala_weight() ->int:
    random_fact = ''
    count       = 0
    position    = 0
    weight      = 0
    while (count < 1000) and (weight == 0):
        # Get random fact
        random_fact = random_koala_fact()
        if 'kg' in random_fact:
            position = random_fact.find('kg')
            weight = int(random_fact[position - 2:position])
        count += 1
    return weight   



# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == '__main__':
    print(random_koala_fact())

    print(unique_koala_facts(10))

    print(num_joey_facts())

    print(koala_weight())
