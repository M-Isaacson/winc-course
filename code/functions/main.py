# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

"""
====================
Exercise: Functions
====================
"""

# 1 --> Greet
def greet(name):
    return 'Hello, ' + name + '!'

#print(greet('Bob'))

# 2 --> add three numbers
def add(number_1,number_2,number_3):
    return number_1 + number_2 + number_3

#print(add(10,12,8))

# 3 --> is it a positive number
def positive(number):
    if (type(number)==int) or (type(number)==float):
        return number > 0

#print(positive(50.3))
#print(positive(-50))
#print(positive(0))

# 4 --> is it a negative number
def negative(number):
    if (type(number)==int) or (type(number)==float):
        return number < 0

#print(negative(50))
#print(negative(-50))
#print(negative(0))

