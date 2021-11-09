# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

"""
==================
Exercise: Casting
==================
"""

# Part 1 --> Leek price printing
leek_price = 2
print('Leek is ' + str(leek_price) + ' euro per kilo.')

# Part 2 --> Leek order
order_38  = 'leek 4'
sum_total = int(order_38[order_38.find(' ')+1:]) * leek_price
print(sum_total)

# Part 3 --> Broccoli price and order
order_39        ='broccoli 1.6'
broccoli_price  = 2.34
sum_total_39    = float(order_39[order_39.find(' ')+1:]) * broccoli_price
print(order_39[order_39.find(' ')+1:] + 'kg broccoli costs ' + str(round(sum_total_39,2)) + 'e')