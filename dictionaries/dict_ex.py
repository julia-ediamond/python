groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08,
}

print(groceries)
# specific value
print(groceries["Baby Spinach"])
# 2.78
groceries["Avocadoes"] = 1.00
print(groceries)

del groceries["Bacon"]
print(groceries)

for item in groceries:
    print(f"{item}: ${groceries[item]}")
    # Baby Spinach: $2.78
# Hot Chocolate: $3.7
# Crackers: $2.1
# Carrots: $0.56
# Oranges: $3.08
# Avocadoes: $1.0
# another way to iterate
for item, price in groceries.items():
    print(f"{item}: {price}")
# same result
