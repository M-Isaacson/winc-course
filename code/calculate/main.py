# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line

# Prices a piece for supermarket items:
broccoli        = 2
leek            = 2
potato          = 3
brussel_sprout  = 7

# Total cost when buying one of each
sum_one_each = broccoli + brussel_sprout + leek + potato
print(sum_one_each)

# Average price per item
avg_price = sum_one_each / 4
print(avg_price)

# Number per item to buy
num_potatoes        = 7
num_broccolis       = 5
num_leeks           = 2
num_brussel_sprouts = 10

# Total costs
sum_total = (broccoli * num_broccolis) + (potato * num_potatoes) + (leek * num_leeks) + (brussel_sprout * num_brussel_sprouts)
print(sum_total)

# Discount
discount_percentage = 30

# Cost after discount
discounted_sum_total = round(sum_total - (sum_total * discount_percentage / 100),2)
print(discounted_sum_total)