# Write a function that takes two parameters;
# the unit price of an item, and how many units were purchased. Return the total cost as a string.
def price(price_per_unit, num_units):
    total_price = price_per_unit * num_units
    return total_price


total_price = price(3.79, 1)
print(f"${total_price}")
