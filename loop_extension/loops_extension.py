groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

user_input = input("How many items have you bought: ")
pay = 0
for items in groceries:
    total_price = int(user_input) * float(items[1])
    #pay = sum(total_price)
    pay += total_price
    print(
        f"You bought {user_input} of {items[0]}, for the price of {total_price}.")

print(f"The total pay is {float(pay)}.")
